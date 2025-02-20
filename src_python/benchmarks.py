import pandas as pd
import timeit
import importlib
import populate
importlib.reload(populate)
from populate import populate_array, populate_list, populate_deque

def runtime_populate(max_power):
    
    runtimes = pd.DataFrame(columns = ['power', 'array', 'list', 'deque'])
    
    for i in range(1, max_power+1):
        n_nums = 10**i
        
        # test array
        start = timeit.default_timer()
        populate_array(n_nums)
        end = timeit.default_timer()
        rt_array = end - start
        
        # test list
        start = timeit.default_timer()
        populate_list(n_nums)
        end = timeit.default_timer()
        rt_list = end - start
        
        # test deque
        start = timeit.default_timer()
        populate_deque(n_nums)
        end = timeit.default_timer()
        rt_deque = end - start
        
        runtimes.loc[i-1] = [i, rt_array, rt_list, rt_deque]
        
    runtimes['power'] = runtimes['power'].astype(int)
    runtimes.set_index('power', inplace=True)
    
    return runtimes
