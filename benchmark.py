import coullide.coullide as cc
import coullide.numpy_coullide as nc

import numpy
import time
time.t0 = time.time()
n_items = 10_000
rmin = 0.005
rmax = 0.05
x_source = numpy.random.random(n_items)
y_source = numpy.random.random(n_items)
z_source = numpy.random.random(n_items)
r_source = rmin + (rmax-rmin)*numpy.random.random(n_items)



def timer(string):
    t1 = time.time()
    dt = t1 - time.t0
    print(f"time elapsed : {dt} | {string}")
    time.t0 = t1

def basic():
    x_save = []
    y_save = []
    z_save = []
    r_save = []
    n_save = 0
    def collides(x,y,z,r,n_save):
        for j in range(n_save):
            if (x_save[j] - x)**2 + (y_save[j] - y)**2 + (z_save[j] - z)**2 < (r_save[j] + r)**2:
                return True
        return False
    
    for i in range(n_items):
        x = x_source[i]
        y = y_source[i]
        z = z_source[i]
        r = r_source[i]

        
        if collides(x,y,z,r,n_save):
            # Skip adding this item if it collides
            continue

        x_save.append(x)
        y_save.append(y)
        z_save.append(z)
        r_save.append(r)
        n_save += 1
    print(f'Saved: {n_save}')
    
def basic_numpy1():
    x_save = []
    y_save = []
    z_save = []
    r_save = []
    n_save = 0
    
    for i in range(n_items):
        x = x_source[i]
        y = y_source[i]
        z = z_source[i]
        r = r_source[i]
        boolean = (numpy.array(x_save) - x)**2 + (numpy.array(y_save) - y)**2 + (numpy.array(z_save) - z)**2 < (numpy.array(r_save) + r)**2
        if numpy.any(boolean):
            continue

        x_save.append(x)
        y_save.append(y)
        z_save.append(z)
        r_save.append(r)
        n_save += 1
    print(f'Saved: {n_save}')


def basic_numpy2():
    x_save = numpy.array([])
    y_save = numpy.array([])
    z_save = numpy.array([])
    r_save = numpy.array([])
    n_save = 0
    
    for i in range(n_items):
        x = x_source[i]
        y = y_source[i]
        z = z_source[i]
        r = r_source[i]
        boolean = ((x_save) - x)**2 + ((y_save) - y)**2 + ((z_save) - z)**2 < ((r_save) + r)**2
        if numpy.any(boolean):
            continue

        x_save = numpy.append(x_save,x)
        y_save = numpy.append(y_save,y)
        z_save = numpy.append(z_save,z)
        r_save = numpy.append(r_save,r)

        n_save += 1
    print(f'Saved: {n_save}')


def basic_numpy3():
    x_save = numpy.zeros(n_items)
    y_save = numpy.zeros(n_items)
    z_save = numpy.zeros(n_items)
    r_save = numpy.zeros(n_items)    
    n_save = 0
    
    for i in range(n_items):
        x = x_source[i]
        y = y_source[i]
        z = z_source[i]
        r = r_source[i]
        boolean = ((x_save[:n_save]) - x)**2 + ((y_save[:n_save]) - y)**2 + ((z_save[:n_save]) - z)**2 < ((r_save[:n_save]) + r)**2
        if numpy.any(boolean):
            continue

        x_save[n_save] = x
        y_save[n_save] = y
        z_save[n_save] = z
        r_save[n_save] = r        

        n_save += 1
    print(f'Saved: {n_save}')



def basic_coullide():
    x_save = []
    y_save = []
    z_save = []
    r_save = []

    collision = cc.Placeholder(rmax)

    collision.distance = cc.pythagoras
    n_save = 0
    
    for i in range(n_items):
        x = x_source[i]
        y = y_source[i]
        z = z_source[i]
        r = r_source[i]

        
        if collision.collides((x,y,z),r):
            continue
        collision.add((x,y,z),r)

        x_save.append(x)
        y_save.append(y)
        z_save.append(z)
        r_save.append(r)
        n_save += 1
    print(f'Saved: {n_save}')


def numpy_coullide():
    x_save = []
    y_save = []
    z_save = []
    r_save = []

    collision = nc.Placeholder(rmax)
    n_save = 0
    
    for i in range(n_items):
        x = x_source[i]
        y = y_source[i]
        z = z_source[i]
        r = r_source[i]

        
        if collision.collides(numpy.array((x,y,z)),r):
            continue
        collision.add(numpy.array((x,y,z)),r)

        x_save.append(x)
        y_save.append(y)
        z_save.append(z)
        r_save.append(r)
        n_save += 1
    #print(len(collision.data))
    #print(list(map(len,collision.data)))
    print(f'Saved: {n_save}')


    




timer("init")

#basic()
#timer("Basic")

basic_numpy1()
timer("Basic Numpy1")

basic_numpy2()
timer("Basic Numpy2")

basic_numpy3()
timer("Basic Numpy3")

basic_coullide()
timer("Basic Coullide")

numpy_coullide()
timer("Numpy Coullide")


""" rmax=0.01
time elapsed : 0.0003609657287597656 | init

Saved: 9286
time elapsed : 69.3267560005188 | Basic

Saved: 9286
time elapsed : 11.595807075500488 | Basic Numpy1

Saved: 87144
time elapsed : 49.26371097564697 | Basic Numpy2

Saved: 87136
time elapsed : 42.80243110656738 | Basic Numpy3

Saved: 87144
time elapsed : 8.90333080291748 | Basic Coullide

Saved: 87144
time elapsed : 32.08146619796753 | Numpy Coullide
"""

"""rmax=0.02:
time elapsed : 0.0003180503845214844 | init

Saved: 7499
time elapsed : 10.020197868347168 | Basic Numpy1

Saved: 7499
time elapsed : 0.4641571044921875 | Basic Numpy2

Saved: 7499
time elapsed : 0.287229061126709 | Basic Numpy3

Saved: 7499
time elapsed : 0.38491392135620117 | Basic Coullide

Saved: 7499
time elapsed : 1.474308967590332 | Numpy Coullide
"""

"""rmax=0.01:
Saved: 9324
time elapsed : 11.539238929748535 | Basic Numpy1
Saved: 9324
time elapsed : 0.5696632862091064 | Basic Numpy2
Saved: 9324
time elapsed : 0.34854578971862793 | Basic Numpy3
Saved: 9324
time elapsed : 0.3901560306549072 | Basic Coullide
Saved: 9324
time elapsed : 1.3118770122528076 | Numpy Coullide
"""

"""rmax=0.1:
Saved: 1711
time elapsed : 3.025104284286499 | Basic Numpy1
Saved: 1711
time elapsed : 0.27940869331359863 | Basic Numpy2
Saved: 1711
time elapsed : 0.24578309059143066 | Basic Numpy3
Saved: 1711
time elapsed : 1.7832210063934326 | Basic Coullide
Saved: 1711
time elapsed : 1.953387975692749 | Numpy Coullide
"""

"""rmax=0.05:
Saved: 3327
time elapsed : 5.454232215881348 | Basic Numpy1
Saved: 3327
time elapsed : 0.2939169406890869 | Basic Numpy2
Saved: 3327
time elapsed : 0.23149609565734863 | Basic Numpy3
Saved: 3327
time elapsed : 0.7843070030212402 | Basic Coullide
Saved: 3327
time elapsed : 2.2859880924224854 | Numpy Coullide
"""


"""
Summary:
Basic Numpy3 is always better than Numpy1 and Numpy2 because of pre-allocating numpy arrays 
It is rarely worth it to try to optimize coullide using Numpy since the number of objects in each bucket is small.
When the number of objects in each bucket is large, basic coullide becomes slow because of looping in python
"""
