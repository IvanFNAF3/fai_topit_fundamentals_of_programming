a = 1000
b = a
c = None

print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b) # Прогноз: True
print("a is b:", a is b) # Прогноз: False
print("a == c:", a == c) # Прогноз: True
print("a is c:", a is c) # Прогноз: False
print("c is None:", c is None)


first = "python"
second = "py" + "thon"

print(f"{id(first)} {id(second)}")
print(first == second)
print(first is second)