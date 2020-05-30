from .utils import price_string_to_number


class SearchItem(object):
    def __init__(self, title, url, published_at, description, price) -> None:
        self.title = title
        self.url = url
        self._published_at = published_at
        self.description = description
        self._price = price_string_to_number(price)

    @property
    def price(self) -> str:
        if self._price:
            return f'{self._price} €'

        return "No price"
