def parse_request(words: list[str]):
    if len(words) == 0:
        print("Вы ничего не ввели!")
    if words[0] == 'student':
        if len(words) != 2:
            print("Количество аргументов больше или меньше 2!")
            return
        if by_student.get(words[1]) == None:
            print("Такого студента не существует!")
            return
        print(by_student[words[1]])
    elif words[0] == 'best':
        if len(words) != 3:
            print("Количество аргументов больше или меньше 3!")
            return
        name, lab = words[1], words[2]
        if best_score.get((name, lab)) == None:
            print("Лучшая оценка не определена для входных данных!")
            return
        print(best_score.get((name, lab)))
    elif words[0] == 'attempts':
            if len(words) != 3:
                print("Количество аргументов больше или меньше 3!")
                return
            name, lab = words[1], words[2]
            if cnt_tries.get((name, lab)) == None:
                print("Число попыток не определено для входных данных!")
                return
            print(cnt_tries.get((name, lab)))
    elif words[0] == 'completed':
            if len(words) != 2:
                print("Количество аргументов больше или меньше 2!")
                return
            if students_by_lab.get(words[1]) == None:
                print("Такой лабораторной не существует или её никто не сдавал!")
                return
            print(students_by_lab[words[1]])
    else:
        print("Такой команды не существует. Есть student, best, attempts, completed")
    

submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

students = {name for name, lab, score in submissions}
labs = {lab for name, lab, score in submissions}

by_student = {}
for name, lab, score in submissions:
    by_student.setdefault(name, []).append((lab, score))

best_score = {}
for name, lab, score in submissions:
    if best_score.setdefault((name, lab), 0) < score:
        best_score[(name, lab)] = score

cnt_tries = {}
for name, lab, score in submissions:
    if cnt_tries.get((name, lab)) == None:
        cnt_tries[(name, lab)] = 0
    cnt_tries[(name, lab)] += 1

students_by_lab = {}
for name, lab, _ in submissions:
    students_by_lab.setdefault(lab, set()).add(name)

both = set.intersection(*students_by_lab.values())

new = ("daria", "lab_02", 4)
name, lab, score = new
submissions.append(new)

students.add(name)
labs.add(lab)

by_student.setdefault(name, []).append((lab, score))

key = (name, lab)
if score > best_score.get(key, -1):
    best_score[key] = score
cnt_tries[key] = cnt_tries.get(key, 0) + 1

students_by_lab.setdefault(lab, set()).add(name)
both = set.intersection(*students_by_lab.values())

print(both)

inp = input("Введите текстовый запрос: ")
words = inp.split(' ')
parse_request(words)
