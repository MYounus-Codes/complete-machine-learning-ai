"""Clean Wikipedia content and export text, images, and links to Excel.

The script reads the previously fetched Wikipedia HTML and writes three sheets:
- text
- images
- links
"""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
from bs4 import BeautifulSoup


BASE_URL = "https://en.wikipedia.org"


def load_html(path: Path) -> str:
    """Read the fetched HTML from disk."""

    return path.read_text(encoding="utf-8")


def extract_text_blocks(soup: BeautifulSoup) -> pd.DataFrame:
    """Collect readable text from headings and paragraphs."""

    rows: list[dict[str, str | int]] = []

    for index, tag in enumerate(soup.find_all(["h1", "h2", "h3", "p"]), start=1):
        text = tag.get_text(" ", strip=True)
        if text:
            rows.append(
                {
                    "order": index,
                    "tag": tag.name,
                    "text": text,
                    "character_count": len(text),
                }
            )

    return pd.DataFrame(rows)


def extract_images(soup: BeautifulSoup) -> pd.DataFrame:
    """Collect image URLs and alt text."""

    rows: list[dict[str, str]] = []

    for index, image in enumerate(soup.find_all("img"), start=1):
        src = image.get("src", "")
        rows.append(
            {
                "order": index,
                "src": urljoin(BASE_URL, src),
                "alt": image.get("alt", ""),
                "title": image.get("title", ""),
            }
        )

    return pd.DataFrame(rows)


def extract_links(soup: BeautifulSoup) -> pd.DataFrame:
    """Collect hyperlink text and absolute URLs."""

    rows: list[dict[str, str]] = []

    for index, link in enumerate(soup.find_all("a"), start=1):
        href = link.get("href", "")
        text = link.get_text(" ", strip=True)
        if href and text:
            rows.append(
                {
                    "order": index,
                    "text": text,
                    "href": urljoin(BASE_URL, href),
                }
            )

    return pd.DataFrame(rows)


def export_to_excel(text_df: pd.DataFrame, images_df: pd.DataFrame, links_df: pd.DataFrame, output_path: Path) -> None:
    """Write the cleaned data into an Excel workbook."""

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        text_df.to_excel(writer, sheet_name="text", index=False)
        images_df.to_excel(writer, sheet_name="images", index=False)
        links_df.to_excel(writer, sheet_name="links", index=False)


def main() -> None:
    """Run the Wikipedia cleaning project."""

    tutorial_dir = Path(__file__).resolve().parent
    html_path = tutorial_dir / "data" / "items.html"
    output_path = tutorial_dir / "exports" / "wikipedia_cleaned.xlsx"

    html = load_html(html_path)
    soup = BeautifulSoup(html, "html.parser")

    text_df = extract_text_blocks(soup)
    images_df = extract_images(soup)
    links_df = extract_links(soup)

    print("Text rows:", len(text_df))
    print("Image rows:", len(images_df))
    print("Link rows:", len(links_df))

    export_to_excel(text_df, images_df, links_df, output_path)
    print("Saved Excel file to:", output_path)


if __name__ == "__main__":
    main()