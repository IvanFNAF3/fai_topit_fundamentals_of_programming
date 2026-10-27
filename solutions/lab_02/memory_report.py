import gc
import tracemalloc
import sys

m1_size = sys.getsizeof([])
m2_size = sys.getsizeof([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
m3_size = sys.getsizeof((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
m4_size = sys.getsizeof("0123456789")
m5_size = sys.getsizeof(1)
m6_size = sys.getsizeof(None)

hunded_list = []
h_sizes = []

h_sizes.append([0, sys.getsizeof(hunded_list)])
for _ in range(0, 100):
    hunded_list.append(30)
    if len(hunded_list) in (0, 4, 8, 16, 24, 32, 40, 52, 64, 76, 92):
        h_sizes.append([len(hunded_list), sys.getsizeof(hunded_list)])

gc.collect()

tracemalloc.start()
tracemalloc.reset_peak()
obj = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

gc.collect()

tracemalloc.start()
tracemalloc.reset_peak()
obj2 = range(100_000)
current2, peak2 = tracemalloc.get_traced_memory()
tracemalloc.stop()

otn = peak / peak2

print("---------Отчёт по памяти----------")
print("------Часть 1. Измерение объема памяти-------")
print("Пустой массив: ", m1_size, " байт")
print("Список из 10 чисел: ", m2_size, " байт")
print("Кортеж из 10 чисел: ", m3_size, " байт")
print("Строка из 10 символов: ", m4_size, " байт")
print("Целое число: ", m5_size, " байт")
print("None: ", m6_size, " байт")
print("\n------Часть 2. Рост объема памяти массива-------")
for val in h_sizes:
    print(f"Количество элементов: {val[0]} Объем памяти: {val[1]} байтов")

print("\n------Часть 3. Range vs List-------")
print("List:")
print("Current: ", current)
print("Peak: ", peak)
print("---------")
print("Range:")
print("Current: ", current2)
print("Peak: ", peak2)
print("Отношение пиковых объемов: ", otn)
print("---------Конец отчёта---------")

