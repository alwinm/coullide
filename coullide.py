from collections import defaultdict
import itertools
import math

def pythagoras(location1,location2):
    return sum((a-b)**2 for a,b in zip(location1,location2))**0.5

class Placeholder:
    def __init__(self, r_max):
        # r_max is the maximum radius of an object
        self.r_max = r_max
        # 2*r_max is the farthest an object can be to collide
        self.bin_size = 2*r_max

        # self.data[index] = list_of_objects
        self.data = defaultdict(list)

    def index(self,location):
        return tuple(math.floor(x / self.bin_size) for x in location)
    
    def collides(self,location,radius):
        # check if object with location and radius collides
        index = self.index(location) 
        
        for d_index in itertools.product((-1,0,1),repeat=len(location)):
            key = tuple(map(sum,zip(index,d_index)))
            for location2,radius2 in self.data[key]:
                if self.distance(location,location2) < radius + radius2:
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

    
