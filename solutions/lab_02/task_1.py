a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

# Эксперимент B
print("------------------")
first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

second = [10, 20, 30]
print(second == first)
print(second is first)

second[0] = 20
print(first, second)

#Практическая задача
print("------------------")
import copy

config1 = {
    "name": "Эксперимент A",
    "participants": ["Алиса", "Боб"],
    "launch_params": [
        {"epochs": 10, "lr": 0.001},
        {"batch_size": 32, "optimizer": "adam"}
    ]
}

print("Исходная config1:")
print(config1)

config2 = config1

config2["participants"].append("Карл")
config2["launch_params"][0]["epochs"] = 999

print("\nПосле изменения config2 простым присваиванием:")
print("config1:", config1)
print("config2:", config2)

assert config1["launch_params"][0]["epochs"] == 999
assert "Карл" in config1["participants"]
print("\nНежелательное совместное изменение подтверждено: config1 и config2 — один объект.")

config1 = {
    "name": "Эксперимент A",
    "participants": ["Алиса", "Боб"],
    "launch_params": [
        {"epochs": 10, "lr": 0.001},
        {"batch_size": 32, "optimizer": "adam"}
    ]
}

config3 = copy.deepcopy(config1)

config3["name"] = "Эксперимент B"
config3["participants"].append("Дина")
config3["launch_params"][0]["epochs"] = 50
config3["launch_params"].append({"dropout": 0.2})

print("\nПосле изменения независимой config3:")
print("config1:", config1)
print("config3:", config3)

assert config3 is not config1

assert config3["participants"] is not config1["participants"]
assert config3["launch_params"] is not config1["launch_params"]
assert config3["launch_params"][0] is not config1["launch_params"][0]

assert config1["name"] == "Эксперимент A"
assert config3["name"] == "Эксперимент B"

assert "Дина" not in config1["participants"]
assert "Дина" in config3["participants"]

assert config1["launch_params"][0]["epochs"] == 10
assert config3["launch_params"][0]["epochs"] == 50

assert len(config1["launch_params"]) == 2
assert len(config3["launch_params"]) == 3

print("\nНезависимость config1 и config3 подтверждена assert-ами.")