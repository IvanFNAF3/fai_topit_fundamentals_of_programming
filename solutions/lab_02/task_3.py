import sys
import weakref

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

print("--------")

# Эксперимент 2
class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

# Практическая задача
class Record:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"Record({self.name!r})"


registry = weakref.WeakValueDictionary()

r1 = Record("one")
r2 = Record("two")

registry["one"] = r1
registry["two"] = r2

tmp = Record ("three")

registry["three"] = tmp


print("До удаления tmp:")
print("- ключи реестра:", list(registry.keys()))
print("- содержимое:", list(registry.items()))

del registry["three"]

print("\nПосле удаления tmp:")
print("ключи реестра:", list(registry.keys()))
print("содержимое:", list(registry.items()))

del r2

print("\nПосле удаления r2:")
print("  ключи реестра:", list(registry.keys()))
print("  содержимое:", list(registry.items()))

print("\nr1 всё ещё существует:", r1)