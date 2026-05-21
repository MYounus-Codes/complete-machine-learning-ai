"""Reusable Python functions with clear examples."""


def greet(name: str) -> str:
    """Return a greeting message."""

    return f"Hello, {name}!"


def add_numbers(first: int, second: int) -> int:
    """Return the sum of two numbers."""

    return first + second


def describe_student(name: str, course: str = "Python") -> str:
    """Use a default argument to simplify the call site."""

    return f"{name} is studying {course}."


def total_with_tax(amount: float, tax_rate: float = 0.15) -> float:
    """Return a price including tax."""

    return amount + (amount * tax_rate)


def show_scope_example() -> None:
    """Demonstrate local scope."""

    message = "Inside the function"
    print(message)


double = lambda value: value * 2  # noqa: E731


def factorial(number: int) -> int:
    """Calculate factorial recursively."""

    if number < 0:
        raise ValueError("number must be non-negative")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


def apply_operation(first: int, second: int, operation) -> int:
    """Accept a function as an argument."""

    return operation(first, second)


if __name__ == "__main__":
    print(greet("Amina"))
    print(add_numbers(4, 6))
    print(describe_student("Amina"))
    print(total_with_tax(100))
    show_scope_example()
    print(double(5))
    print(factorial(5))
    print(apply_operation(8, 2, add_numbers))