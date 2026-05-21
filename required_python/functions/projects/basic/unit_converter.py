"""Basic project for functions: convert simple units with reusable functions."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""

    return (celsius * 9 / 5) + 32


def kilometers_to_miles(kilometers: float) -> float:
    """Convert kilometers to miles."""

    return kilometers * 0.621371


def main() -> None:
    """Run the starter project."""

    print("20C in Fahrenheit:", round(celsius_to_fahrenheit(20), 2))
    print("5 km in miles:", round(kilometers_to_miles(5), 2))


if __name__ == "__main__":
    main()