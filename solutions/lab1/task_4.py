student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print(student[0])

print(student[3])
print(student[:4])
print(student[5:])
print(student.upper())
print(student.lower())
print(student[0] + "." + " " + student[5] + ".")
print(course[::-1])

print("%s - %s: %d/%d (%s%%)" % (student, course, completed, total, f"{((completed / total) * 100):.1f}"))
print("{} - {}: {}/{} ({:.1f}%)".format(student, course, completed, total, completed / total * 100))
print(f"{student} - {course}: {completed}/{total} ({completed / total * 100}%)")

symbol = "Я"
# symbol[0] = "д"
print(symbol)
print(ord(symbol))
print(chr(ord(symbol)))
print(symbol.encode("utf-8"))
print(len(symbol.encode("utf-8")))