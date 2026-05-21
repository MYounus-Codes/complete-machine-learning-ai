# BeautifulSoup Tutorial

This folder is a small, practical BeautifulSoup learning path. It starts with the basics of parsing HTML and ends with a real project that cleans a Wikipedia page and exports the results to Excel.

## Learning order

1. `01_basic_bs4.py` - create a soup object and inspect tags, strings, and attributes.
2. `02_searching_and_filters.py` - find tags with `find`, `find_all`, `select`, and filters.
3. `03_navigation_and_mutation.py` - move through the parse tree and modify elements.
4. `04_advanced_parsing.py` - learn parser choices, `SoupStrainer`, and text cleanup.
5. `05_wikipedia_clean_to_excel.py` - clean Wikipedia content and save it into Excel sheets.

## Files and folders

- `sample.html` - small local HTML page for safe practice.
- `data/items.html` - fetched Wikipedia HTML used by the project and generated locally.
- `exports/` - created by the project script when the Excel file is written.

## What each lesson covers

- Basic object inspection: `title`, `body`, `name`, `attrs`, `string`, `text`, `get_text`, `prettify`.
- Search methods: `find`, `find_all`, `select`, `select_one`, regex filters, callables, and keyword attributes.
- Tree navigation and mutation: `parent`, `children`, `descendants`, `next_sibling`, `previous_sibling`, `new_tag`, `append`, `insert`, `replace_with`, `wrap`, `unwrap`, `extract`, `decompose`.
- Advanced parsing: parser selection, `original_encoding`, `SoupStrainer`, and normalization helpers.
- Real project output: separate text, image, and link data into pandas DataFrames and export them to Excel.

## Running the code

Use the virtual environment Python from the workspace root:

```powershell
& D:/compplete-machine-learning-ai/.venv/Scripts/python.exe data-collection[web-scraping]/beautifulsoup-tutorial/01_basic_bs4.py
& D:/compplete-machine-learning-ai/.venv/Scripts/python.exe data-collection[web-scraping]/beautifulsoup-tutorial/05_wikipedia_clean_to_excel.py
```

## Notes

- The scripts are written to be easy to read first and then extend.
- The Wikipedia project reads the fetched HTML from `data/items.html`.
- The Excel export uses pandas DataFrames and writes one sheet per data type.
- Generated files stay local and are ignored by git.