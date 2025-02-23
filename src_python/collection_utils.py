import random
import timeit
from array import array
from collections import deque

random.seed(82)

# super class
class collectionTest(object):
    tests = []
    
    def __init__(self, length, collection, rt_populate):
        self.length = length
        self.type = type(collection).__name__
        self.collection = collection
        self.runtimes = {
            'populate': rt_populate
        }
        
        collectionTest.tests.append(self)

# subclasses for each collection type
class arrayTest(collectionTest):
    def __init__(self, length):        
        start = timeit.default_timer()
        a = array('i', [0] * length)
        for i in range(length):
            # a[i] = rng.integers(0, length)
            a[i] = random.randint(0, length)
        end = timeit.default_timer()
        
        rt_populate = end - start
        
        super().__init__(length, a, rt_populate)

class listTest(collectionTest):
    def __init__(self, length):
        start = timeit.default_timer()
        l = [None] * length
        for i in range(length):
            # l[i] = rng.integers(0, length)
            l[i] = random.randint(0, length)
        end = timeit.default_timer()
        
        rt_populate = end - start
        
        super().__init__(length, l, rt_populate)
        
class dequeTest(collectionTest):
    def __init__(self, length):
        start = timeit.default_timer()
        d = deque([], maxlen=length)
        for i in range(length):
            # d.append(rng.integers(0, length))
            d.append(random.randint(0, length))
        end = timeit.default_timer()
        
        rt_populate = end - start
        
        super().__init__(length, d, rt_populate)


def make_collections(max_length: int, scale = 10):
    length = 10
    while length < max_length:
        arrayTest(length)
        listTest(length)
        dequeTest(length)
        length = length*scale
    arrayTest(max_length)
    listTest(max_length)
    dequeTest(max_length)
