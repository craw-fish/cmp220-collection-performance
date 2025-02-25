import numpy as np
import pandas as pd
import timeit
import importlib
global_seed = 82
import collection_utils
import benchmarks
import graph_results
importlib.reload(collection_utils)
importlib.reload(benchmarks)
importlib.reload(graph_results)
from collection_utils import make_collections, collectionTest
from benchmarks import sort_items, filter_items, insert_item
from graph_results import graph_results

total_start = timeit.default_timer()

# perform benchmarks multiple times, compile results into list of df's
n_trials = 5
all_results = []
for i in range(n_trials):
    print(f"Running trial {i+1} of {n_trials}...")
    results_i = pd.DataFrame(columns=['benchmark', 'length_log', 'array', 'list', 'deque'])
    # multi-index: benchmark outside, length inside (for each benchmark, show results of each length)
    results_i.set_index(['benchmark', 'length_log'], inplace=True)
    
    # instantiate collections; also records 'populate' runtime
    print("\tPopulating collections...")
    make_collections(max_length=10**8, interval_scale=2)
    print("\tCollections populated.")
    
    print("\tRunning benchmarks...")
    for test in collectionTest.tests:
        # run benchmarks
        sort_items(test)
        filter_items(test)
        insert_item(test)
        # add runtime results to df
        for benchmark, runtime in test.runtimes.items():
            results_i.loc[(benchmark, np.log10(test.length)), test.type] = runtime
    print("\tBenchmarks completed.")
    
    # empty list of collection tests
    collectionTest.tests.clear()      
    
    results_i = results_i.unstack(level=1).stack(future_stack=True)
    all_results.append(results_i)

total_end = timeit.default_timer()
print("All trials completed.")
print(f"Total runtime: {total_end - total_start:.3f}s ({1000 * (total_end - total_start):.0f}ms)")

# average of all generated dataframes
avg_results = pd.concat(all_results).groupby(level=['benchmark', 'length_log'], sort=False).mean()
# log runtime values
avg_results_log = avg_results.map(np.log10)

# save to excel spreadsheet
with pd.ExcelWriter('../results/runtime.xlsx', mode='a', if_sheet_exists='replace') as writer:
    avg_results.to_excel(writer, sheet_name='python')
    avg_results_log.to_excel(writer, sheet_name='python_log')

# graph original and log df
graph_results(avg_results, is_log=False, save_graphs=True)
graph_results(avg_results_log, is_log=True, save_graphs=True)
