"""Practice exercises for Python data types."""


def is_string(text: object) -> bool:
    """Return True when the value is a string."""

    return isinstance(text, str)


def convert_temperature(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""

    return (celsius * 9 / 5) + 32


def unique_count(values: list[int]) -> int:
    """Count unique values in a list."""

    return len(set(values))


def make_student(name: str, course: str, active: bool) -> dict[str, object]:
    """Create a small student record."""

    return {"name": name, "course": course, "active": active}


def run_exercises() -> None:
    """Display exercise results."""

    print("Is 'hello' a string?", is_string("hello"))
    print("20C in Fahrenheit:", convert_temperature(20))
    print("Unique values:", unique_count([1, 1, 2, 3, 3, 4]))
    print("Student record:", make_student("Amina", "Python", True))


if __name__ == "__main__":
    run_exercises()