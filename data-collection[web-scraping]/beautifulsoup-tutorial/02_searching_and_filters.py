"""BeautifulSoup searching patterns and filters.

This file shows how to use common search arguments in a practical way.
"""

from __future__ import annotations

import re
from pathlib import Path

from bs4 import BeautifulSoup


def load_soup() -> BeautifulSoup:
    """Load the local sample HTML into BeautifulSoup."""

    sample_path = Path(__file__).resolve().parent / "sample.html"
    html = sample_path.read_text(encoding="utf-8")
    return BeautifulSoup(html, "html.parser")


def search_by_names(soup: BeautifulSoup) -> None:
    """Search by tag name and multiple matches."""

    print("All paragraphs:", soup.find_all("p"))
    print("All headings:", soup.find_all(["h1", "h2", "h3"]))
    print("First list item:", soup.find("li"))


def search_by_attributes(soup: BeautifulSoup) -> None:
    """Search by id, class, and arbitrary attributes."""

    print("By id:", soup.find(id="page-title"))
    print("By class:", soup.find(class_="lead"))
    print("All anchors with href:", soup.find_all("a", href=True))
    print("Select one content div:", soup.select_one("div.content"))


def search_with_filters(soup: BeautifulSoup) -> None:
    """Use regex, callables, text, and limits."""

    print("Regex headings:", soup.find_all(re.compile(r"^h[1-6]$")))
    print("Text search:", soup.find_all(string=re.compile("BeautifulSoup")))
    print("Limited results:", soup.find_all("a", limit=1))

    def has_internal_link(tag) -> bool:
        """Return True for relative links."""

        return tag.name == "a" and tag.get("href", "").startswith("/")

    print("Callable filter:", soup.find_all(has_internal_link))


def search_with_css_selectors(soup: BeautifulSoup) -> None:
    """Use CSS selectors with select and select_one."""

    print("All links:", soup.select("a"))
    print("Lead paragraph:", soup.select_one("p.lead"))
    print("List items:", soup.select("ul li"))


def main() -> None:
    """Run the search examples."""

    soup = load_soup()
    search_by_names(soup)
    search_by_attributes(soup)
    search_with_filters(soup)
    search_with_css_selectors(soup)


if __name__ == "__main__":
    main()