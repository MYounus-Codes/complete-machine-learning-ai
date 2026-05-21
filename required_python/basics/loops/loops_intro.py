"""Beginner-friendly loop examples.

Read this file from top to bottom. Each function focuses on one small idea.
"""


def show_for_loop() -> None:
    """Repeat a task with a for loop."""

    for number in range(1, 6):
        print(f"Counting up: {number}")


def show_for_loop_over_list() -> None:
    """Loop through a list one item at a time."""

    fruits = ["apple", "banana", "mango"]

    for fruit in fruits:
        print(f"Fruit: {fruit}")


def show_while_loop() -> None:
    """Repeat while a condition is true."""

    remaining_steps = 3

    while remaining_steps > 0:
        print(f"Steps left: {remaining_steps}")
        remaining_steps -= 1


def show_break_and_continue() -> None:
    """Show how to stop a loop or skip one round."""

    for number in range(1, 8):
        if number == 3:
            print("Skipping 3")
            continue

        if number == 6:
            print("Stopping at 6")
            break

        print(f"Number: {number}")


def show_nested_loops() -> None:
    """Demonstrate loops inside loops."""

    for row in range(1, 4):
        for column in range(1, 4):
            print(f"row {row}, column {column}")


def show_enumerate() -> None:
    """Loop with both item and position."""

    names = ["Amina", "Zoya", "Sara"]

    for position, name in enumerate(names, start=1):
        print(f"{position}. {name}")


if __name__ == "__main__":
    show_for_loop()
    show_for_loop_over_list()
    show_while_loop()
    show_break_and_continue()
    show_nested_loops()
    show_enumerate()