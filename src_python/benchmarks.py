import random
import copy
import timeit
import importlib
import collection_utils
importlib.reload(collection_utils)
from collection_utils import collectionTest
from collections_demo import global_seed

random.seed(global_seed)

def insert_items(test):
    # deep copy (don't update original collection)
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
