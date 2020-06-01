import math
import re  # The regex module - do not google it and don't go there now :)
from typing import List


def price_string_to_number(price_string: str) -> float:
    # How do we get the number from the string
    # Think of the two possible values here and Google NaN value in Python :)
    raise NotImplemented


def results_to_models(results: List[str]) -> List[object]:
    # Convert search result list to objects
    raise NotImplemented


def model_to_csv(item: object) -> List[str]:
    # Convert a SearchItem models to a list with strings
    # that we can write to a csv
    raise NotImplemented


def csv_to_model(csv: List[str]) -> object:
    # Convert a csv row to a SearchItem model
    raise NotImplemented


def clean_string(text: str) -> str:
    """Removes multiple new lines and unnecessary whitespaces"""
    remove_characters = re.compile(r"[\n ]{2,}")

    cleaned_rows = []

    for line in text.splitlines():
        if line:
            cleaned_line = re.sub(remove_characters, "", line)
            cleaned_rows.append(cleaned_line.strip())

    return "\n".join(cleaned_rows)
