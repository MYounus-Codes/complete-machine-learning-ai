"""Medium project for functions: analyze and clean text."""


def normalize_text(text: str) -> str:
    """Lowercase the text and remove extra spaces."""

    return " ".join(text.lower().split())


def count_words(text: str) -> int:
    """Count words in a text string."""

    normalized = normalize_text(text)

    if not normalized:
        return 0

    return len(normalized.split())


def most_common_length(words: list[str]) -> int:
    """Return the length that appears most often in the list."""

    if not words:
        return 0

    lengths: dict[int, int] = {}

    for word in words:
        length = len(word)
        lengths[length] = lengths.get(length, 0) + 1

    most_common = 0
    highest_count = 0

    for length, count in lengths.items():
        if count > highest_count:
            highest_count = count
            most_common = length

    return most_common


def main() -> None:
    """Run the medium project."""

    sentence = "Python functions make code simple and reusable"
    words = sentence.split()

    print("Normalized:", normalize_text(sentence))
    print("Word count:", count_words(sentence))
    print("Most common word length:", most_common_length(words))


if __name__ == "__main__":
    main()