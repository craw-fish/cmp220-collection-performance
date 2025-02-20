import numpy as np
import timeit
from array import array
from collections import deque

# seeded random number generator
rng = np.random.default_rng(seed=82)

# super class
class collectionTest(object):
    tests = []
    
    def __init__(self, power, collection, rt_populate):
        self.power = power
        self.type = type(collection).__name__
        self.collection = collection
        self.runtimes = {
            'populate': rt_populate
        }
        
        collectionTest.tests.append(self)

# subclasses for each collection type
class arrayTest(collectionTest):
    def __init__(self, power):
        length = 10**power
        
        start = timeit.default_timer()
        a = array('i', [0] * length)
        for i in range(length):
            a[i] = rng.integers(0, length)
        end = timeit.default_timer()
        
        rt_populate = end - start
        
        super().__init__(power, a, rt_populate)

class listTest(collectionTest):
    def __init__(self, power):
        length = 10**power
        
        start = timeit.default_timer()
        l = [None] * length
        for i in range(length):
            l[i] = rng.integers(0, length)
        end = timeit.default_timer()
        
        rt_populate = end - start
        
        super().__init__(power, l, rt_populate)
        
class dequeTest(collectionTest):
    def __init__(self, power):
        length = 10**power
        
        start = timeit.default_timer()
        d = deque([], maxlen=length)
        for i in range(length):
            d.append(rng.integers(0, length))
        end = timeit.default_timer()
        
        rt_populate = end - start
        
        super().__init__(power, d, rt_populate)


def make_collections(power: int):
    for i in range(1, power + 1):
        arrayTest(i)
        listTest(i)
        dequeTest(i)
