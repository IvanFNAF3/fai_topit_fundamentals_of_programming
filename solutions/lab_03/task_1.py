def get_grade(result, work_type, misses, students_by_level) -> str:
    if not(0 <= result <= 100):
        print("Ошибка! Результат ученика выходит за границы от 0 до 100!")
        return ""
    if not(0 <= misses <= 5):
        print("Ошибка! Количество пропусков выходит за границы от 0 до 5!")
        return ""
    levels = ["недостаточный", "удовлетворительный", "хороший", "отличный"]
    cur_ind = 0
    if result >= 90:
        cur_ind = 3
    elif result >= 75:
        cur_ind = 2
    elif result >= 60:
        cur_ind = 1
    else:
        cur_ind = 0

    if misses > 3 and cur_ind > 0:
        cur_ind -= 1
    level = levels[cur_ind]
    students_by_level[cur_ind] += 1

    real_work_type = ""
    match work_type:
        case "exam":
            real_work_type = "Экзаменационная работа"
        case "project":
            real_work_type = "Проектная работа"
        case "practice":
            real_work_type = "Практическая работа"
        case _:
            real_work_type = "Неизвестный тип работы"
    return "Тип работы: " + str(real_work_type) + " Оценка: " + str(level) + "\n"

n = int(input("Введите количество студентов: "))
print("Введите результат, тип работы и количество пропусков через пробел для каждого студента")
students_by_level = [0, 0, 0, 0]
grade_types = ["недостаточный", "удовлетворительный", "хороший", "отличный"]
individual_results = ""

for i in range(0, n):
    result, work_type, absences = input().split()
    result = int(result)
    absences = int(absences)

    individual_results += get_grade(result, work_type, absences, students_by_level)

print("Индивидуальные результаты:")
print(individual_results)
print("Количество студентов по результатам:")
for i in range(0, 4):
    print(grade_types[i] + ": " + str(students_by_level[i]))
