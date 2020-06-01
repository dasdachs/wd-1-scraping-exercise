from typing import List

# from .scraper import search
from .model import SearchItem

# from .utils import models_to_csv, results_to_models


__all__ = ["execute_search", "save_to_csv"]


PATH_TO_DATA = "data"


def execute_search(search_text: str) -> List[SearchItem]:
    raise NotImplemented


def save_to_csv(results: List[SearchItem]) -> None:
    # Save models to a csv file
    raise NotImplemented
