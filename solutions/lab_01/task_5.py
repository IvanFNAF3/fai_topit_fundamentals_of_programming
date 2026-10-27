"""Программа для экспериментов
Данная программа запрашивает значения эксперимента:
имя исследователя
имя эксперимента
количество запусков
длительность запуска
действительная и мнимая часть комплексного числа
В конце программа должна выдать следующую информацию:
Название эксперимента
Имя исследователя
Количество запусков
Длительность всех запусков в секундах и минутах
Коэффициент комплексного числа
Квадрат модуля комплексного числа
Есть ли выполненные запуски
Также в конце программа выводит типы шести введенных значений.
"""

explorer_name = input("Имя исследователя: ")
experiment_name = input("Имя эксперимента: ")
runs_count = int(input("Количество выполненны запусков: "))
run_time = float(input("Длительность одного запуска в секундах: "))
real_value = float(input("Действительная честь комплексного числа: "))
imag_value = float(input("Мнимая честь комплексного числа: "))

total_time_sec = run_time * runs_count
total_time_min = total_time_sec / 60
complex_num = complex(real_value, imag_value)
module_square = real_value ** 2 + imag_value ** 2
has_runs = bool(runs_count)

print("========================================")
print(f"ЭКСПЕРИМЕНТ: {experiment_name}")
print(f"Исследователь: {explorer_name}")
print(f"Запуски: {runs_count}")
print(f"Общее время: {total_time_sec} с ({total_time_min:.2f} мин)")
print(f"Коэффициент: {complex_num}")
print(f"Квадрат модуля: {module_square:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print("========================================")

print("Тип имени исследователя:", type(explorer_name))
print("Тип названия эксперимента:", type(experiment_name))
print("Тип количества запусков:", type(runs_count))
print("Тип времени запуска:", type(run_time))
print("Тип реальной части числа:", type(real_value))
print("Тип мнимой части комплексного числа:", type(imag_value))