"""BeautifulSoup basics: create a soup object and inspect HTML.

This file focuses on the most common BeautifulSoup attributes and methods.
"""

from pathlib import Path

from bs4 import BeautifulSoup


def load_html(path: Path) -> str:
    """Read HTML from a file using UTF-8."""

    return path.read_text(encoding="utf-8")


def explore_basic_attributes(soup: BeautifulSoup) -> None:
    """Show the most common BeautifulSoup attributes."""

    print("Top-level title:", soup.title)
    print("Title text:", soup.title.string if soup.title else None)
    print("Page body tag:", soup.body)
    print("Body tag name:", soup.body.name if soup.body else None)
    print("First h1 attrs:", soup.h1.attrs if soup.h1 else None)
    print("Prettified HTML:\n", soup.prettify()[:400])


def explore_text_helpers(soup: BeautifulSoup) -> None:
    """Show text-related methods and properties."""

    paragraph = soup.find("p")

    print("Paragraph tag:", paragraph)
    print("Paragraph string:", paragraph.string if paragraph else None)
    print("Paragraph text:", paragraph.text if paragraph else None)
    print("Paragraph get_text:", paragraph.get_text(strip=True) if paragraph else None)
    print("All text:", soup.get_text(" ", strip=True)[:200])
    print("Strings generator sample:", list(soup.stripped_strings)[:8])


def explore_tag_lookup(soup: BeautifulSoup) -> None:
    """Show tag lookup helpers like find and find_all."""

    print("Find h1:", soup.find("h1"))
    print("Find by id:", soup.find(id="page-title"))
    print("Find all links:", soup.find_all("a"))
    print("Find one link with href:", soup.find("a", href=True))


def main() -> None:
    """Run the basic BeautifulSoup examples."""

    sample_path = Path(__file__).resolve().parent / "sample.html"
    html = load_html(sample_path)
    soup = BeautifulSoup(html, "html.parser")

    explore_basic_attributes(soup)
    explore_text_helpers(soup)
    explore_tag_lookup(soup)


if __name__ == "__main__":
    main()