from typing import Dict, List

import requests
from bs4 import BeautifulSoup


__all__ = ["search"]

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


def extract_content_from_html(html_string: str) -> List[Dict]:
    """Parses and extracts data from html"""
    # Comment out and finish the code
    raise NotImplementedError  # Delete this

    # soup = BeautifulSoup(html_string, "html.parser")
    # items = soup.find_all({{ html_tag }}, class_="{{class name}}")
    #
    # parsed_items = []
    #
    # for item in items:
    #     title = item.find(class_="{{ title_class }}").getText()
    #
    #     a_tag = item.find("a", href=True)
    #     url = f'{BASE_URL}{a_tag["href"]}'
    #
    #     description = item.find(class_="{{ description_class }}").getText()
    #     published_at = item.find("time", class_="{{ published_at_class }}").getText()
    #     price = item.find("time", class_="{{ published_at_class }}").getText()
    # parsed_item = {
    #     "title": title,
    #     "url": url,
    #     "description": description,
    #     "published_at": published_at,
    #     "price": price
    # }
    # parsed_items.append(parsed_item)
    #
    # return parsed_items


def search(search_text: str) -> Dict:
    # Combine requests and both helper functions
    # search_url = prepare_url(?)
    # request = requests.get(?)
    # items = extract_content_from_html(?)
    # return items
    raise NotImplementedError  # Delete this
