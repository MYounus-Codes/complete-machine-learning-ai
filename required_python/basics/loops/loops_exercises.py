"""Short loop exercises for beginners."""


def count_to_ten() -> list[int]:
    """Return numbers from 1 to 10."""

    numbers: list[int] = []

    for number in range(1, 11):
        numbers.append(number)

    return numbers


def even_numbers(limit: int) -> list[int]:
    """Return even numbers up to the limit."""

    evens: list[int] = []

    for number in range(1, limit + 1):
        if number % 2 == 0:
            evens.append(number)

    return evens


def total_characters(words: list[str]) -> int:
    """Count all characters in a list of words."""

    total = 0

    for word in words:
        total += len(word)

    return total


def repeat_word(word: str, times: int) -> str:
    """Repeat a word several times with spaces."""

    output = ""

    for _ in range(times):
        output += word + " "

    return output.strip()


def run_exercises() -> None:
    """Print the answers so the learner can compare results."""

    print("Count to ten:", count_to_ten())
    print("Even numbers:", even_numbers(12))
    print("Character total:", total_characters(["python", "loops", "fun"]))
    print("Repeat word:", repeat_word("practice", 3))


if __name__ == "__main__":
    run_exercises()