CATEGORIES = (
    "отличный",
    "хороший",
    "удовлетворительный",
    "недостаточный",
    "нет данных",
)
NO_DATA = "нет данных"


def mean(values: list[float]) -> float | None:
    if not values:
        return None

    total = 0.0
    for value in values:
        total += value
    return total / len(values)


def minimum(values: list[float]) -> float | None:
    if not values:
        return None

    result = values[0]
    for value in values[1:]:
        if value < result:
            result = value
    return result


def maximum(values: list[float]) -> float | None:
    if not values:
        return None

    result = values[0]
    for value in values[1:]:
        if value > result:
            result = value
    return result


def classify(score: float | None) -> str:
    if score is None:
        return NO_DATA
    if not 0 <= score <= 100:
        raise ValueError("score должен быть в диапазоне от 0 до 100 или None")

    if score >= 90:
        return "отличный"
    if score >= 75:
        return "хороший"
    if score >= 60:
        return "удовлетворительный"
    return "недостаточный"


def student_summary(name: str, results: list[float]) -> dict:
    avg = mean(results)
    return {
        "name": name,
        "count": len(results),
        "mean": avg,
        "minimum": minimum(results),
        "maximum": maximum(results),
        "category": classify(avg),
    }


def find_top_students(students: dict[str, list[float]]) -> list[str]:
    means: dict[str, float] = {}
    for name, results in students.items():
        if results:
            avg = mean(results)
            if avg is not None:
                means[name] = avg

    if not means:
        return []

    best = None
    for value in means.values():
        if best is None or value > best:
            best = value

    return [name for name, value in means.items() if abs(value - best) < 1e-9]


def group_summary(students: dict[str, list[float]]) -> dict:
    summaries: dict[str, dict] = {}
    category_counts = {category: 0 for category in CATEGORIES}
    students_without_results: list[str] = []

    total_sum = 0.0
    total_count = 0

    for name, results in students.items():
        summary = student_summary(name, results)
        summaries[name] = summary
        category_counts[summary["category"]] += 1

        if results:
            for score in results:
                total_sum += score
                total_count += 1
        else:
            students_without_results.append(name)

    group_mean = total_sum / total_count if total_count else None

    rating = sorted(
        (name for name, summary in summaries.items() if summary["mean"] is not None),
        key=lambda student_name: summaries[student_name]["mean"],
        reverse=True,
    )

    return {
        "students": summaries,
        "group_mean": group_mean,
        "category_counts": category_counts,
        "top_students": find_top_students(students),
        "rating": rating,
        "total_students": len(students),
        "total_results": total_count,
        "students_without_results": students_without_results,
    }


def _fmt_number(value: float | None) -> str:
    return "NullValue" if value is None else f"{value:.2f}"


def format_report(student_data: dict[str, dict], group_data: dict) -> str:
    lines = ["Отчёт по учебным результатам", "=" * 40]

    if not student_data:
        lines.append("Студентов нет.")
    else:
        for name, summary in student_data.items():
            lines.append(
                f"{name}: средний={_fmt_number(summary['mean'])}, "
                f"min={_fmt_number(summary['minimum'])}, "
                f"max={_fmt_number(summary['maximum'])}, "
                f"категория={summary['category']}"
            )

    lines.append("")
    lines.append(f"Средний результат группы: {_fmt_number(group_data.get('group_mean'))}")
    lines.append(f"Всего студентов: {group_data.get('total_students', len(student_data))}")
    lines.append(f"Всего результатов: {group_data.get('total_results', 0)}")

    top_students = group_data.get("top_students", [])
    lines.append("Лидер(ы): " + (", ".join(top_students) if top_students else "нет"))

    rating = group_data.get("rating", [])
    if rating:
        rating_text = ", ".join(
            f"{name} ({_fmt_number(student_data[name]['mean'])})"
            for name in rating
        )
        lines.append(f"Рейтинг: {rating_text}")

    lines.append("Категории:")
    for category in CATEGORIES:
        count = group_data.get("category_counts", {}).get(category, 0)
        lines.append(f"  {category}: {count}")

    without_results = group_data.get("students_without_results", [])
    if without_results:
        lines.append("Без результатов: " + ", ".join(without_results))

    return "\n".join(lines)


def run_scenarios() -> None:
    # 1. Обычный набор данных
    normal_students = {
        "Анна": [78, 91, 84, 88],
        "Борис": [60, 72, 68],
        "Дарья": [95, 93, 97, 90],
        "Илья": [55, 61],
    }
    normal = group_summary(normal_students)
    assert abs(normal["group_mean"] - 1032 / 13) < 1e-9
    assert normal["top_students"] == ["Дарья"]
    assert normal["category_counts"]["отличный"] == 1
    assert normal["category_counts"]["хороший"] == 1
    assert normal["category_counts"]["удовлетворительный"] == 1
    assert normal["category_counts"]["недостаточный"] == 1

    # 2. Один студент
    one_student = group_summary({"A": [100]})
    assert one_student["group_mean"] == 100.0
    assert one_student["top_students"] == ["A"]

    # 3. Несколько лидеров
    multiple_leaders = group_summary({
        "Анна": [80, 90],
        "Борис": [85, 85],
        "Владимир": [70],
    })
    assert multiple_leaders["top_students"] == ["Анна", "Борис"]

    # 4. Пустая группа
    empty_group = group_summary({})
    assert empty_group["group_mean"] is None
    assert empty_group["top_students"] == []
    assert empty_group["total_students"] == 0
    assert empty_group["total_results"] == 0

    # 5. Студент без результатов
    with_empty_student = group_summary({"Анна": [], "Борис": [60]})
    assert with_empty_student["students"]["Анна"]["category"] == "нет данных"
    assert with_empty_student["students"]["Анна"]["mean"] is None
    assert with_empty_student["students_without_results"] == ["Анна"]
    assert with_empty_student["top_students"] == ["Борис"]

    # 6. Граничные значения категорий
    boundary = group_summary({
        "Анна": [59],
        "Борис": [60],
        "Владимир": [75],
        "Дмитрий": [90],
        "Евгений": [100],
    })
    assert boundary["category_counts"]["недостаточный"] == 1
    assert boundary["category_counts"]["удовлетворительный"] == 1
    assert boundary["category_counts"]["хороший"] == 1
    assert boundary["category_counts"]["отличный"] == 2

    # Дополнительно: проверка classify на границах
    assert [classify(x) for x in (0, 59, 60, 74, 75, 89, 90, 100)] == [
        "недостаточный",
        "недостаточный",
        "удовлетворительный",
        "удовлетворительный",
        "хороший",
        "хороший",
        "отличный",
        "отличный",
    ]

    print("Все проверки задания 5 пройдены.")


def main() -> None:
    students = {
        "Анна": [78, 91, 84, 88],
        "Борис": [60, 72, 68],
        "Дарья": [95, 93, 97, 90],
        "Илья": [55, 61],
    }

    group_data = group_summary(students)
    print(format_report(group_data["students"], group_data))
    print()
    run_scenarios()


if __name__ == "__main__":
    main()