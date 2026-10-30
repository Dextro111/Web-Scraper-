# Web Scraper

A simple Python web scraper project that fetches Wikipedia pages, extracts the page title, and follows related Wikipedia links to continue scraping.

## What this project does

- Sends an HTTP request to a page using `requests`
- Parses the HTML with `BeautifulSoup`
- Finds the page title (`firstHeading`)
- Collects links from the article content
- Follows a random Wikipedia article link
- Stops after a limited depth to avoid endless recursion

## Technologies used

- Python 3
- `requests`
- `beautifulsoup4`

## Project structure

```text
Web Scraper/
├── scraper.py
├── env/
├── README.md
└── requirements.txt
```

## Setup

If you are using the existing virtual environment:

```bash
cd "Web Scraper"
source env/bin/activate
```

If you need to recreate the environment:

```bash
cd "Web Scraper"
python3 -m venv env
source env/bin/activate
pip install requests beautifulsoup4
```

## Run the scraper

```bash
cd "Web Scraper"
source env/bin/activate
python scraper.py
```

## Notes

- This project is for learning and educational use.
- Wikipedia may block aggressive scraping or automated requests, so using a browser-like `User-Agent` helps.
- Always respect a site's `robots.txt` and terms of service.
- The recursive scraping is intentionally limited to avoid infinite loops.

## Main file

- `scraper.py` contains the scraping logic.

## Example output

```text
Web scraping
Wikipedia for the Web
...
```

## License

This project is intended for educational use.
