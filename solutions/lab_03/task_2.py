import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def linear_search(arr, target):
    start = time.perf_counter()
    end = 0
    cnt = 0
    for i in range(0, len(arr)):
        cnt += 1
        if arr[i] == target:
            end = time.perf_counter()
            print(f"Линейный поиск с массивом с {len(arr)} элементами.\n\t- Время: {end - start:.6f} мс.\n\t Сравнений: {cnt}")
            return i
    end = time.perf_counter()
    print(f"Линейный поиск с массивом с {len(arr)} элементами.\n\t- Время: {end - start:.6f} мс.\n\t Сравнений: {cnt}")
    return -1

def binary_search(arr, target):
    start = time.perf_counter()
    low = 0
    high = len(arr) - 1
    cnt = 0

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        cnt += 1
        if guess == target:
            end = time.perf_counter()
            print(f"Бинарный поиск с массивом с {len(arr)} элементами.\n\t- Время: {end - start:.6f} с.\n\t Сравнений: {cnt}")
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    end = time.perf_counter()
    print(f"Бинарный поиск с массивом с {len(arr)} элементами.\n\t- Время: {end - start:.6f} с.\n\t Сравнений: {cnt}")
    return -1

measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

sumi = 0
mini = measurements[0]
maxi = measurements[0]
chets = 0
arith_mean = 0.0
gt_mean = 0

for val in measurements:
    sumi += val

for val in measurements:
    if mini > val:
        mini = val

for val in measurements:
    if maxi < val:
        maxi = val

for val in measurements:
    if val % 2 == 0:
        chets += 1

cnt = 0
arith_sumi = 0
for val in measurements:
    cnt += 1
    arith_sumi += val

mean = arith_sumi / cnt

for val in measurements:
    if val > mean:
        gt_mean += 1

print("Массив: " + str(measurements))
print("Сумма: " + str(sumi))
print("Минимальное значение: " + str(mini))
print("Максимальное значение: " + str(maxi))
print("Кол-во четных чисел: " + str(chets))
print("Кол-во чисел больших чем ср. ариф.: " + str(gt_mean))

f = int(input(("Введите число для поиска в массиве: ")))
res = -1
for i in range(0, len(measurements)):
    if measurements[i] == f:
        res = i
        break
print("Первое вхождение: " + str(res))

num = int(input("Введите число для проверки на простоту: "))
isprime = True;
if num <= 1:
    print("Число не простое")
    isprime = False
if isprime:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Число не простое")
            isprime = False
            break
if isprime:
    print("Число простое")

ten_arr = list(range(1, 11))
hundred_arr = list(range(1, 101))
thousand_arr = list(range(1, 1001))

linear_search(ten_arr, 7)
binary_search(ten_arr, 7)
linear_search(hundred_arr, 78)
binary_search(hundred_arr, 78)
linear_search(thousand_arr, 789)
binary_search(thousand_arr, 789)