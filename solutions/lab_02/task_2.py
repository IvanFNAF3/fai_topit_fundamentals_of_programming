import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

original.append(["Databases", 5])

print("Original:")
print(original)
print("Alias:")
print(alias)
print("Shallow:")
print(shallow)
print("Deep:")
print(deep)
print("\nid Внешних список: \nid original: ", id(original))
print("id alias: ", id(alias))
print("id shallow: ", id(shallow))
print("id deep: ", id(deep))
print("\nid Первого вложенного списка: \nid original: ", id(original[0]))
print("id alias: ", id(alias[0]))
print("id shallow: ", id(shallow[0]))
print("id deep: ", id(deep[0]))
print("\nid Первой оценки: \nid original: ", id(original[0][1]))
print("id alias: ", id(alias[0][1]))
print("id shallow: ", id(shallow[0][1]))
print("id deep: ", id(deep[0][1]))

original[0][1] = 3

print("\n\nOriginal:")
print(original)
print("Alias:")
print(alias)
print("Shallow:")
print(shallow)
print("Deep:")
print(deep)
print("\nid Внешних список: \nid original: ", id(original))
print("id alias: ", id(alias))
print("id shallow: ", id(shallow))
print("id deep: ", id(deep))
print("\nid Первого вложенного списка: \nid original: ", id(original[0]))
print("id alias: ", id(alias[0]))
print("id shallow: ", id(shallow[0]))
print("id deep: ", id(deep[0]))
print("\nid Первой оценки: \nid original: ", id(original[0][1]))
print("id alias: ", id(alias[0][1]))
print("id shallow: ", id(shallow[0][1]))
print("id deep: ", id(deep[0][1]))

#Неправильное создание
wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1

print("wrong_matrix:")
for row in wrong_matrix:
    print(row)

print("\nid строк wrong_matrix:")
print([id(row) for row in wrong_matrix])

assert wrong_matrix[0] is wrong_matrix[1] is wrong_matrix[2]

# Правильное создание
correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1

print("\ncorrect_matrix:")
for row in correct_matrix:
    print(row)

print("\nid строк correct_matrix:")
print([id(row) for row in correct_matrix])

assert correct_matrix[0] is not correct_matrix[1]
assert correct_matrix[1] is not correct_matrix[2]
assert correct_matrix[0] is not correct_matrix[2]