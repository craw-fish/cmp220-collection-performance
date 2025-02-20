import numpy as np
from array import array
from collections import deque

# seed random number generator
rng = np.random.default_rng(seed=82)

def populate_array(length:int):
    # instantiate empty integer array of specified length
    a = array('i', [0] * length)
    
    # fill array with random ints up to value of n
    for i in range(length):
        a[i] = rng.integers(0, length)
        
    return a
    
def populate_list(length:int):
    l = [None] * length
    
    for i in range(length):
        l[i] = rng.integers(0, length)
        
    return l

def populate_deque(length:int):
    d = deque([], maxlen=length)
    
    for i in range(length):
        d.append(rng.integers(0, length))
        
    return d
