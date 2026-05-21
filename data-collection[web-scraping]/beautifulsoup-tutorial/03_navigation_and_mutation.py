"""BeautifulSoup navigation and mutation examples.

This file shows how to move around the parse tree and change it safely.
"""

from __future__ import annotations

from pathlib import Path

from bs4 import BeautifulSoup


def load_soup() -> BeautifulSoup:
    """Load the local sample HTML."""

    sample_path = Path(__file__).resolve().parent / "sample.html"
    html = sample_path.read_text(encoding="utf-8")
    return BeautifulSoup(html, "html.parser")


def show_navigation(soup: BeautifulSoup) -> None:
    """Inspect parent/child/sibling relationships."""

    lead = soup.select_one("p.lead")
    content = soup.select_one("div.content")

    if lead is not None:
        print("Parent:", lead.parent.name)
        print("Next sibling:", lead.next_sibling)
        print("Previous sibling:", lead.previous_sibling)
        print("Next element:", lead.next_element)
        print("Previous element:", lead.previous_element)

    if content is not None:
        print("Children:", list(content.children))
        print("Descendants sample:", list(content.descendants)[:8])


def show_mutation(soup: BeautifulSoup) -> None:
    """Modify the tree using common mutation methods."""

    content = soup.select_one("div.content")
    if content is None:
        return

    new_note = soup.new_tag("p")
    new_note.string = "This note was added with new_tag and append."
    content.append(new_note)

    first_link = soup.find("a")
    if first_link is not None:
        first_link.replace_with(soup.new_tag("strong"))
        strong_tag = soup.find("strong")
        if strong_tag is not None:
            strong_tag.string = "First link replaced with strong tag."

    extra_note = soup.new_tag("p")
    extra_note.string = "Inserted before the list."
    ul_tag = soup.find("ul")
    if ul_tag is not None:
        ul_tag.insert_before(extra_note)

    temp_tag = soup.new_tag("span")
    temp_tag.string = "Temporary content"
    content.append(temp_tag)
    temp_tag.extract()

    removable = soup.new_tag("div")
    removable.string = "This content will be removed."
    content.append(removable)
    removable.decompose()

    print("Mutated HTML preview:\n", soup.prettify()[:500])


def main() -> None:
    """Run the navigation and mutation examples."""

    soup = load_soup()
    show_navigation(soup)
    show_mutation(soup)


if __name__ == "__main__":
    main()