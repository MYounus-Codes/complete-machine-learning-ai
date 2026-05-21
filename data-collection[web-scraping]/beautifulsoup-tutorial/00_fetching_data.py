from pathlib import Path

import requests


def fetch_data(url, path):
    """Fetch data from a URL and save it to a file."""

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(response.text, encoding="utf-8")

url = "https://en.wikipedia.org/wiki/Iran%E2%80%93Israel_proxy_conflict"


fetch_data(url, "data-collection[web-scraping]/beautifulsoup-tutorial/data/items.html")
    