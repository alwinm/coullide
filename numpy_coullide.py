from collections import defaultdict
import itertools
import math
import numpy

def pythagoras(location1,location2):
    return sum((a-b)**2 for a,b in zip(location1,location2))**0.5


class NumpyList:
    def __init__(self):
        self.capacity = 0
        self.length = 0
        self.data = numpy.array([])

    def __iter__(self):
        for x in self.data:
            yield x
        
        
    def append(self,item):
        location,radius = item
        # item should be (coords,r)
        if self.length >= self.capacity:
            # reallocate array
            self.itemlen = len(location) + 1
            
            temporary = self.data
            
            self.data = numpy.zeros([self.capacity*2+10,self.itemlen])

            if self.length:
                self.data[:self.length] = temporary
            
            self.capacity = len(self.data)
            
        self.data[self.length,:-1] = location
        self.data[self.length,-1] = radius
        self.length += 1


    def check(self,location,radius):
        if not self.length:
            return False
        return numpy.any(numpy.sum((self.data[:self.length,:-1] - location)**2,axis=1) < (radius + self.data[:self.length,-1])**2)
        

class Placeholder:
    def __init__(self, r_max):
        # r_max is the maximum radius of an object
        self.r_max = r_max
        # 2*r_max is the farthest an object can be to collide
        self.bin_size = 2*r_max

        # self.data[index] = list_of_objects
        self.data = defaultdict(NumpyList)

    def index(self,location):
        return tuple(numpy.floor(location / self.bin_size).astype(int))
    
    def collides(self,location,radius):
        # check if object with location and radius collides
        index = self.index(location) 
        
        for d_index in itertools.product((-1,0,1),repeat=len(location)):
            key = tuple(map(sum,zip(index,d_index)))

            if self.data[key].check(location,radius):
                return True

        return False

    def add(self,location,radius):
        index = self.index(location)
        self.data[index].append((location,radius))

    def safe_add(self,location,radius):
        if radius > r_max:
            raise Exception("Attempted to add item with radius > r_max")
        self.add(location,radius)

    def rebuild_in_place(self, r_max):
        # rebuild data according to new, larger value of r_max
        if r_max < self.r_max:
            print("ABORT: attempted to rebuild with r_max < self.r_max")
            return

        temporary = []
        for key in self.data:
            for item in self.data[key]:
                temporary.append(item)

        self.data = defaultdict(list)
        
        for location,radius in temporary:
            self.add(location,radius)

    
