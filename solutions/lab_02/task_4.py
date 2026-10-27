import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print("\nИнформация о сборщике мусора (gc)")
print("Доступен ли gc: ", gc.isenabled())
print("Порог поколений: ", gc.get_threshold())
print("Статистика поколений:")
stats = gc.get_stats()
for i, stat in enumerate(stats):
    print(f"\tПоколение {i}: {stat}")

print(id(first), id(second))

del first
del second

print(gc.collect())

print("--------")

# Доп. эксперимент
print("Дополнительный эксперимент")

gc.disable()
print("Автосборка включена: ", gc.isenabled())

try:
    cycles = []

    for i in range(5):
        a = []
        b = []
        a.append(b)
        b.append(a)
        cycles.append((a, b))

    print(f"Создано циклических структур: {len(cycles)}")

    del a, b
    del cycles

    print("Внешние ссылки удалены")

    collected = gc.collect()
    print("gc.collect() вернул:", collected)

finally:
    gc.enable()
    print("Автосборка включена: ", gc.isenabled())

# Практическая задача
print("---------\nПрактическая задача")

gc.disable()
try:
    gc.collect()
    collected_before = gc.collect()
    print(f"1. gc.collect() ДО создания графа: собрано {collected_before} объектов")

    A = {"name": "A", "edges": []}
    B = {"name": "B", "edges": []}
    C = {"name": "C", "edges": []}
    D = {"name": "D", "edges": []} 

    A["edges"].append(B)
    B["edges"].append(C)
    C["edges"].append(A)

    def show(node):
        targets = [e["name"] for e in node["edges"]]
        return f"{node['name']} -> {', '.join(targets) if targets else '—'}"

    print("\n. Связи в графе:")
    for node in (A, B, C, D):
        print("  ", show(node))

    del A, B, C

    collected_after = gc.collect()
    print(f"\n3. gc.collect() ПОСЛЕ удаления внешних имён циклических узлов: "
          f"собрано {collected_after} объектов")

    print(f"\n4. Независимый узел D по-прежнему доступен: {show(D)}")
finally:
    gc.enable()
    print("\nАвтосборка восстановлена:", gc.isenabled())
