import pandas as pd
import timeit
import importlib
import collection_utils
import benchmarks
importlib.reload(collection_utils)
importlib.reload(benchmarks)
from collection_utils import make_collections, collectionTest
from benchmarks import insert_items

total_start = timeit.default_timer()

# perform benchmarks multiple times, compile results into list of df's
n_trials = 3
all_results = []
for i in range(n_trials):
    results_i = pd.DataFrame(columns=['length', 'benchmark', 'array', 'list', 'deque'])
    # multi-index: benchmark outside, length inside (for each benchmark, show results of each length)
    results_i.set_index(['benchmark', 'length'], inplace=True)
    
    # instantiate collections; also records 'populate' runtime
    make_collections(max_length=10**6, scale=10)

    for test in collectionTest.tests:
        # run benchmarks
        insert_items(test)
        # add runtime results to df
        for benchmark, runtime in test.runtimes.items():
            results_i.loc[(benchmark, test.length), test.type] = runtime
    
    # empty list of collection tests
    collectionTest.tests.clear()      
    
    results_i = results_i.unstack(level=1).stack(future_stack=True)
    all_results.append(results_i)

# average of all generated dataframes
avg_results = pd.concat(all_results).groupby(level=['benchmark', 'length'], sort=False).mean()
print(avg_results)

total_end = timeit.default_timer()
print(f"\nRuntimes averaged across {n_trials} trial(s)."
      f"\nTotal runtime: {total_end - total_start:.3f}s ({1000 * (total_end - total_start):.0f}ms)")