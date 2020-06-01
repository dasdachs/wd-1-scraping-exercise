import datetime
import math
from typing import List

from .utils import price_string_to_number


class SearchItem(object):
    def __init__(
        self, title: str, url: str, published_at: str, description: str, price: str
    ) -> None:
        self.title: str = title
        self.url: str = url
        # Convert to datetime and remove the current self.published_at
        # self.published_at: datetime.datetime =  published_at
        self.published_at: str = published_at  # Change start to self.published_at
        self.description: str = description
        self._price: str = price
        self.price: float = price_string_to_number(price)

    def price_str(self) -> str:
        """Add currency to the price data or return TDB (to be discussed)."""
        if self.price != math.nan:
            return f"{self.price} €"

        return "TBD"

    def serialize_to_csv(self) -> List[str]:
        # Return all the data as a row in a csv file
        raise NotImplemented

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __repr__(self) -> str:
        """The representation in the code"""
        return (
            f'SearchItem(title="{self.title}", url="{self.url}", published_at="{self.published_at}",'
            f'description="{self.description}", price="{self._price}")'
        )
