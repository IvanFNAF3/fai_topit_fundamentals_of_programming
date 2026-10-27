import gc
import tracemalloc
import sys

gc.collect()

tracemalloc.start()
tracemalloc.reset_peak()
obj = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Range:")
print("Current: ", current)
print("Peak: ", peak)

gc.collect()

tracemalloc.start()
tracemalloc.reset_peak()
obj2 = range(100_000)
current2, peak2 = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("List(range):")
print("Current: ", current2)
print("Peak: ", peak2)