"""Basic loop project: countdown timer."""


def countdown(start: int) -> None:
    """Count down from the given number to zero."""

    while start >= 0:
        print(start)
        start -= 1

    print("Lift off!")


def main() -> None:
    """Run the beginner countdown project."""

    countdown(5)


if __name__ == "__main__":
    main()