"""A simple calculator built with functions."""


def add(first: float, second: float) -> float:
    return first + second


def subtract(first: float, second: float) -> float:
    return first - second


def multiply(first: float, second: float) -> float:
    return first * second


def divide(first: float, second: float) -> float:
    if second == 0:
        raise ValueError("second must not be zero")
    return first / second


def main() -> None:
    """Run the calculator project."""

    first_number = 12
    second_number = 4

    print("Add:", add(first_number, second_number))
    print("Subtract:", subtract(first_number, second_number))
    print("Multiply:", multiply(first_number, second_number))
    print("Divide:", divide(first_number, second_number))


if __name__ == "__main__":
    main()