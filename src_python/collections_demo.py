import pandas as pd
import importlib
import collection_utils
importlib.reload(collection_utils)
from collection_utils import make_collections, collectionTest

# perform benchmarks multiple times, compile results into list of df's
all_results = []
for i in range(3):
    results_i = pd.DataFrame(columns=['length', 'benchmark', 'array', 'list', 'deque'])
    # multi-index: benchmark outside, length inside (for each benchmark, show results of each length)
    results_i.set_index(['benchmark', 'length'], inplace=True)

    make_collections(max_length=10**6, scale=10)

    # fill df with results
    for test in collectionTest.tests:
        results_i.loc[('populate', test.length), test.type] = test.runtimes['populate']

    results_i = results_i.unstack(level=1).stack(future_stack=True)
    all_results.append(results_i)

# average of all dataframes
avg_results = pd.concat(all_results).groupby(level=['benchmark', 'length']).mean()
avg_results