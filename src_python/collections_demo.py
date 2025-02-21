import pandas as pd
import importlib
import collection_utils
importlib.reload(collection_utils)
from collection_utils import make_collections, collectionTest

results = pd.DataFrame(columns=['length', 'benchmark', 'array', 'list', 'deque'])
# multi-index: benchmark outside, length inside (for each benchmark, show results of each length)
results.set_index(['benchmark', 'length'], inplace=True)

make_collections(max_length=10**7, scale=2)

# fill df with results
for test in collectionTest.tests:
    results.loc[('populate', test.length), test.type] = test.runtimes['populate']

print(results)
