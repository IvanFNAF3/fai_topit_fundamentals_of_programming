import sys
import tracemalloc

print("Размер пустого списка: ", sys.getsizeof([]))
print("Размер списка из 10 чисел: ", sys.getsizeof([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print("Размер кортежа из 10 чисел: ", sys.getsizeof((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)))
print("Размер строки из 10 символов: ", sys.getsizeof("0123456789"))
print("Размер целого числа: ", sys.getsizeof(1))
print("Размер объекта None: ", sys.getsizeof(None))

hunded_list = []

print("Список с 0 эл-ов: ", sys.getsizeof(hunded_list))
for _ in range(0, 100):
    hunded_list.append(30)
    if len(hunded_list) in (0, 4, 8, 16, 24, 32, 40, 52, 64, 76, 92):
        print(f"Список с {len(hunded_list)} эл-ов: ", sys.getsizeof(hunded_list))

# Tracemalloc
print("---------\nTracemalloc:")
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



print("\nРазмер самого объекта range не зависит от N:")
for n in (0, 10, 1_000_000, 10**12):
    print(f"  sys.getsizeof(range({n})) = {sys.getsizeof(range(n))} байт")

print("\nlen(numbers_list) =", len(obj))
print("numbers_list[999] =", obj[999])
print("numbers_range[999] =", obj2[999])