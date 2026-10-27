from math import isclose

# Эксперимент A
x = 17
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

print("-----")

# Эксперимент B
print(2 ** 1000)

print("-----")

# Эксперимент C
result = 0.1 + 0.2

print(result)
print(result == 0.3)
print(result - 0.3)
print(isclose(result, 0.3))

print("-----")

# Эксперимент D
print(int("42"))
print(float("3.14"))
print(str(2026))
print(bool(0))
print(bool(-1))
print(bool(""))
print(bool("False"))
print(complex(2, -3))
print(complex(2, -3).real)
print(complex(2, -3).imag)