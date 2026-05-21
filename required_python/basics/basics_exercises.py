"""Short exercises for Python basics."""


def exercise_1() -> str:
    """Return a greeting message."""

    user_name = "Student"
    return f"Hello, {user_name}!"


def exercise_2(number: int) -> bool:
    """Check whether a number is even."""

    return number % 2 == 0


def exercise_3(items: list[str]) -> int:
    """Return how many items are in the list."""

    return len(items)


def exercise_4(score: int) -> str:
    """Return a simple pass/fail label."""

    return "Pass" if score >= 50 else "Fail"


def run_exercises() -> None:
    """Print the exercise results."""

    print(exercise_1())
    print("Is 8 even?", exercise_2(8))
    print("Item count:", exercise_3(["a", "b", "c"]))
    print("Result:", exercise_4(73))


if __name__ == "__main__":
    run_exercises()