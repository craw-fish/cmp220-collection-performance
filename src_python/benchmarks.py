import random
import copy
import timeit
from collections_demo import global_seed

random.seed(global_seed)

def sort_items(test):
    collection = copy.deepcopy(test.collection)
    
    start = timeit.default_timer()
    sorted(collection)
    end = timeit.default_timer()
    test.runtimes['sort'] = (end - start) * 1000
    
def filter_items(test):
    collection = copy.deepcopy(test.collection)
    
    start = timeit.default_timer()
    # filter for multiples of 10
    filter(lambda x: x % 10 == 0, collection)
    end = timeit.default_timer()
    test.runtimes['filter'] = (end - start) * 1000
    
def insert_item(test):
    collection = copy.deepcopy(test.collection)
    item = random.randint(0, test.length)
    
    insertion_to_idx = {
        'insert start': 0,
        'insert middle': round(len(collection) / 2),
        'insert end': len(collection)
    }
    
    for insertion, idx in insertion_to_idx.items():
        start = timeit.default_timer()
        collection.insert(idx, item)
        end = timeit.default_timer()
        test.runtimes[insertion] = (end - start) * 1000
