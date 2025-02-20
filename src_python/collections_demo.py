import pandas as pd
import importlib
import collection_utils
importlib.reload(collection_utils)
from collection_utils import make_collections, collectionTest

results = pd.DataFrame(columns=['power', 'benchmark', 'array', 'list', 'deque'])
# multi-index: benchmark outside, power inside (for each benchmark, show results of each power)
results.set_index(['benchmark', 'power'], inplace=True)

make_collections(6)

# fill df with results
for test in collectionTest.tests:
    results.loc[('populate', test.power), test.type] = test.runtimes['populate']

print(results)
