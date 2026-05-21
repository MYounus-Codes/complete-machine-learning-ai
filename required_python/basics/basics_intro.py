"""Core Python basics with short, commented examples.

This file is designed to be read top-to-bottom and run section-by-section.
"""


def show_variables() -> None:
    """Demonstrate variables and simple output."""

    name = "Amina"
    age = 21
    height_in_meters = 1.68

    print("Name:", name)
    print("Age:", age)
    print("Height:", height_in_meters)


def show_operators() -> None:
    """Demonstrate arithmetic and comparison operators."""

    first_number = 10
    second_number = 3

    print("Addition:", first_number + second_number)
    print("Subtraction:", first_number - second_number)
    print("Multiplication:", first_number * second_number)
    print("Division:", first_number / second_number)
    print("Floor division:", first_number // second_number)
    print("Remainder:", first_number % second_number)
    print("Power:", first_number**second_number)
    print("Is greater:", first_number > second_number)


def show_conditionals(score: int) -> None:
    """Print a grade message based on score."""

    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    else:
        print("Keep practicing")


def show_loops() -> None:
    """Demonstrate for and while loops."""

    for number in range(1, 6):
        print("For loop value:", number)

    countdown = 3
    while countdown > 0:
        print("While loop value:", countdown)
        countdown -= 1


def show_strings_and_collections() -> None:
    """Demonstrate strings, lists, and dictionaries."""

    language = "python"
    print("Uppercase:", language.upper())
    print("Slice:", language[:3])

    fruits = ["apple", "banana", "mango"]
    fruits.append("orange")
    print("List:", fruits)

    student = {"name": "Amina", "course": "Python", "level": "Beginner"}
    print("Dictionary:", student)
    print("Student name:", student["name"])


def safe_division() -> None:
    """Show simple exception handling."""

    try:
        result = 10 / 0
        print(result)
    except ZeroDivisionError:
        print("You cannot divide by zero.")


if __name__ == "__main__":
    show_variables()
    show_operators()
    show_conditionals(85)
    show_loops()
    show_strings_and_collections()
    safe_division()