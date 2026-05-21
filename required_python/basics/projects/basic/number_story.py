"""Basic project for Python basics: explore numbers and simple decisions."""


def analyze_number(number: int) -> str:
    """Describe a number using simple basics concepts."""

    if number == 0:
        return "The number is zero."

    if number > 0:
        if number % 2 == 0:
            return f"{number} is a positive even number."
        return f"{number} is a positive odd number."

    return f"{number} is a negative number."


def main() -> None:
    """Run the starter project with a few example values."""

    sample_numbers = [7, 12, 0, -3]

    for number in sample_numbers:
        print(analyze_number(number))


if __name__ == "__main__":
    main()