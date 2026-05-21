"""Medium project for Python basics: track student progress."""


def grade_from_score(score: int) -> str:
    """Convert a numeric score to a grade label."""

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def build_progress_report(students: list[dict[str, int | str]]) -> list[str]:
    """Create a report line for each student."""

    report_lines: list[str] = []

    for student in students:
        name = str(student["name"])
        score = int(student["score"])
        grade = grade_from_score(score)
        status = "passed" if score >= 50 else "needs more practice"

        report_lines.append(f"{name}: score {score}, grade {grade}, {status}")

    return report_lines


def main() -> None:
    """Run the medium project."""

    students = [
        {"name": "Amina", "score": 92},
        {"name": "Zoya", "score": 76},
        {"name": "Sara", "score": 48},
    ]

    for line in build_progress_report(students):
        print(line)


if __name__ == "__main__":
    main()