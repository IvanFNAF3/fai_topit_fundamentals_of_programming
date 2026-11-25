def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    sumi = 0
    cnt = 0
    for val in values:
        sumi += val
        cnt += 1
    return sumi / cnt

def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    parts = name.split(' ')
    new_parts = []
    for part in parts:
        if part == "":
            continue
        new_parts.append(part)
    res = ""
    for part in new_parts:
        res += part[:1].upper() + part[1:].lower() + " "
    return res[:len(res) - 1]


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""
    st = f"{prefix}:\n"
    st += f"Имя студента: {normalize_name(student)}\n"
    st += f"Результаты: {str(results)}\n"
    arith_mean = s = f"{arithmetic_mean(results):.{precision}f}"
    st += (f"Среднее арифметическое: {arith_mean}\n")

    return st



def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    result = []
    seen = set()

    for tag in tags:
        cleaned = tag.strip()
        if lowercase:
            cleaned = cleaned.lower()

        if not cleaned:
            continue

        if cleaned not in seen:
            seen.add(cleaned)
            result.append(cleaned)

    return tuple(result)

def add_result(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results

assert arithmetic_mean([1, 2, 3]) == 2.0, 'Incorrect'
assert arithmetic_mean(values=[1, 6]) == 3.5, 'Incorrect'
assert arithmetic_mean([8]) == 8.0, 'Incorrect'

assert normalize_name("  АннА    ПЕтРоВа   МИХайлОвнА   ") == "Анна Петрова Михайловна", 'Incorrect'
assert normalize_name(name="  JOHN   PeTrOv  ") == "John Petrov", 'Incorrect'
assert normalize_name("AAAAABBBB") == "Aaaaabbbb", 'Incorrect'

assert (build_report("  АннА    ПЕтРоВа   МИХайлОвнА   ", [5, 5, 4, 4, 3], precision=1, prefix="Отчет") == "Отчет:\nИмя студента: Анна Петрова Михайловна\nРезультаты: [5, 5, 4, 4, 3]\nСреднее арифметическое: 4.2\n"), 'Incorrect'
assert (build_report("  АннА    ПЕтРоВа   МИХайлОвнА   ", [5, 5, 4, 4, 3], precision=3) == "Результат:\nИмя студента: Анна Петрова Михайловна\nРезультаты: [5, 5, 4, 4, 3]\nСреднее арифметическое: 4.200\n"), 'Incorrect'
assert (build_report("  ИвАн    ЛоЛоЛо   МИХаЙЛлОвнА   ", [5, 5, 4, 4, 3], prefix="Prefix") == "Prefix:\nИмя студента: Иван Лололо Михайлловна\nРезультаты: [5, 5, 4, 4, 3]\nСреднее арифметическое: 4.20\n"), 'Incorrect'

tags_test = ['Hello', '', 'WOrld', '!!!', '', '']
_dict = {"lowercase": False}

assert collect_tags(*tags_test, **_dict) == ('Hello', 'WOrld', '!!!'), 'Incorrect'
assert collect_tags('Hello', '', 'WOrld', '!!!', '', '') == ('hello', 'world', '!!!'), 'Incorrect'
assert collect_tags('Hello', '', 'WOrld', '!!!', 'aAa', lowercase=True) == ('hello', 'world', '!!!', 'aaa'), 'Incorrect'

# print(build_report("  АннА    ПЕтРоВа   МИХайлОвнА   ", [5, 5, 4, 4, 3], precision=1, prefix="Отчет"))

# Фрагмент с LEGB

course = "Python"

def foo():
    course = "Programming"

    def bar():
        nonlocal course
        course = "Fundamental of Programming"
        print(course)

    bar()
    print(course)

foo()
print(course)

def apply_to_results(operation, values):
    """Применяет операцию к каждому элементу последовательности."""
    return [operation(value) for value in values]

# Именованная функция
def is_positive(result):
    return result > 0

reses = [5, 5, 4, 4, 3]

print(apply_to_results(is_positive, reses))

print(apply_to_results(lambda r: r >= 4, reses))

def make_threshold_checker(threshold):
    def check(result):
        return result >= threshold
    return check

check_4 = make_threshold_checker(4)
check_5 = make_threshold_checker(5)

print(apply_to_results(check_4, reses))
print(apply_to_results(check_5, reses))

print([r for r in reses if check_4(r)])
print([r for r in reses if check_5(r)])