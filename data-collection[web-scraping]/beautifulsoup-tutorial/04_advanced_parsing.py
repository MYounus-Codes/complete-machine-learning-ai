"""Advanced BeautifulSoup parsing techniques.

This file covers parser selection, encoding, SoupStrainer, and cleaning helpers.
"""

from __future__ import annotations

from pathlib import Path

from bs4 import BeautifulSoup, SoupStrainer


def load_html(path: Path) -> str:
    """Read a file as HTML text."""

    return path.read_text(encoding="utf-8")


def parse_with_different_parsers(html: str) -> None:
    """Show how parser choice changes the soup object."""

    for parser_name in ("html.parser", "lxml", "html5lib"):
        try:
            soup = BeautifulSoup(html, parser_name)
            print(f"Parser: {parser_name}")
            print("Original encoding:", soup.original_encoding)
            print("Title:", soup.title.string if soup.title else None)
        except Exception as exc:
            print(f"Parser {parser_name} unavailable: {exc}")


def parse_with_strainer(html: str) -> None:
    """Limit parsing to a subset of tags using SoupStrainer."""

    only_links = SoupStrainer("a")
    soup = BeautifulSoup(html, "html.parser", parse_only=only_links)
    print("Strained links:", soup.find_all("a"))


def clean_text(html: str) -> list[str]:
    """Return a compact list of cleaned text lines."""

    soup = BeautifulSoup(html, "html.parser")
    lines: list[str] = []

    for text in soup.stripped_strings:
        if text:
            lines.append(text)

    return lines


def main() -> None:
    """Run the advanced parsing examples."""

    sample_path = Path(__file__).resolve().parent / "sample.html"
    html = load_html(sample_path)

    parse_with_different_parsers(html)
    parse_with_strainer(html)
    print("Cleaned text sample:", clean_text(html))


if __name__ == "__main__":
    main()