"""Short exercises for Python functions."""


def square(number: int) -> int:
    """Return the square of a number."""

    return number * number


def is_even(number: int) -> bool:
    """Check whether a number is even."""

    return number % 2 == 0


def average(values: list[float]) -> float:
    """Return the average of a list of numbers."""

    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)


def welcome_message(name: str, city: str = "your city") -> str:
    """Return a message with a default city value."""

    return f"Welcome {name} from {city}!"


def run_exercises() -> None:
    """Print exercise outputs."""

    print("Square:", square(7))
    print("Even:", is_even(10))
    print("Average:", average([10, 20, 30]))
    print(welcome_message("Amina", "Lahore"))


if __name__ == "__main__":
    run_exercises()