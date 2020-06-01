from typing import Dict, List

import requests
from bs4 import BeautifulSoup

from .utils import clean_string

BASE_URL = "https://www.bolha.com"


def prepare_url(search_text: str) -> str:
    raise NotImplementedError  # Delete this
    # Comment out and finish the code
    # Query is the part of the URL that start with a "?"
    # followed by a key value part
    # Multiple query parameters can be separated with "&"
    # example.com?name=janez&surname=novak

    # query_start =                 # Insert the start of the query from bolha.com
    # formatted_search =            # Spaces are not allowed so separate multiple word with +
    # query = f'{query_start}{formatted_search}'
    # return f'{BASE_URL}/{query}'
    # Test with: python -m pytest tests/test_scraper.py::test_prepare_url


def extract_content_from_html(html_string: str) -> List[Dict]:
    """Parses and extracts data from html"""
    # Comment out and finish the code
    # raise NotImplementedError  # Delete this

    # soup = BeautifulSoup(html_string, "html.parser")
    # items = soup.find_all("{{ html_tag }}", class_="{{ class of the element }}")
    #
    # parsed_items = []
    #
    # for item in items:
    #     if item.find("time"):
    #         title = item.find(class_="{{ class of the element }}").getText()
    #
    #         a_tag = item.find("a", href=True)
    #         url = f'{BASE_URL}{a_tag["href"]}'
    #
    #         description = item.find(class_="{{ class of the element }}").getText()
    #         published_at = item.find("{{ special html tag for dates and time }}")["datetime"]
    #         price = item.find(class_="{{ class of the element }}").getText()
    #
    #         parsed_item = {
    #             "title": clean_string(title),
    #             "url": url,
    #             "description": clean_string(description),
    #             "published_at": published_at,
    #             "price": clean_string(price),
    #         }
    #         parsed_items.append(parsed_item)
    #
    # return parsed_items
    # Test with: python -m pytest tests/test_scraper.py::test_extract_content_from_html


def search(search_text: str) -> List[Dict]:
    raise NotImplementedError  # Delete this
    # Combine requests and both helper functions
    # search_url = prepare_url(?)
    # request = requests.get(?)
    # items = extract_content_from_html(request.?)
    #
    # return items
    # Test with: python -m pytest tests/test_scraper.py::test_search
