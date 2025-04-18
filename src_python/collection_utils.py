import random
import timeit
from array import array
from collections import deque
from collections_demo import global_seed

random.seed(global_seed)

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
            a[i] = random.randint(0, length)
        end = timeit.default_timer()
        
        rt_populate = (end - start) * 1000
        
        super().__init__(length, a, rt_populate)

class listTest(collectionTest):
    def __init__(self, length):
        start = timeit.default_timer()
        l = [None] * length
        for i in range(length):
            l[i] = random.randint(0, length)
        end = timeit.default_timer()
        
        rt_populate = (end - start) * 1000
        
        super().__init__(length, l, rt_populate)
        
class dequeTest(collectionTest):
    def __init__(self, length):
        start = timeit.default_timer()
        d = deque([])
        for i in range(length):
            d.append(random.randint(0, length))
        end = timeit.default_timer()
        
        rt_populate = (end - start) * 1000
        
        super().__init__(length, d, rt_populate)


def make_collections(max_length: int, interval_scale = 10):
    length = interval_scale
    while length < max_length:
        arrayTest(length)
        listTest(length)
        dequeTest(length)
        length = length * interval_scale
    arrayTest(max_length)
    listTest(max_length)
    dequeTest(max_length)
