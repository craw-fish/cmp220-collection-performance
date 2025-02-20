import pandas as pd
import importlib
import benchmarks
importlib.reload(benchmarks)
from benchmarks import runtime_populate

rt_populate = runtime_populate(max_power=6)
print(rt_populate)
