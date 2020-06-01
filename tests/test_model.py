import datetime
import math

import pytests

from src.model import SearchItem


@pytest.mark.parametrize(
    (
        "title",
        "url",
        "published_at",
        "description",
        "price",
        "expected_published_at",
        "expected_price",
        "expected_price_string",
    ),
    [
        (
            "HARRY POTTER",
            "https://www.bolha.com/kocke/harry-potter-oglas-3877893",
            "2020-05-01T20:00:00+02:00",
            "Prodam lego kocke Harry Potter komplet, je odlicno ohranjen!",
            "75\xa0€",
            datetime.datetime.fromisoformat("2020-05-01T20:00:00+02:00"),
            75.0,
            "75.0 €",
        ),
        (
            "HARRY POTTER",
            "https://www.bolha.com/kocke/harry-potter-oglas-3877893",
            "2020-05-31T20:00:00+02:00",
            "Prodam lego kocke Harry Potter komplet, je odlicno ohranjen!",
            "Cena po dogvoru",
            datetime.datetime.fromisoformat("2020-05-31T20:00:00+02:00"),
            math.nan,
            "TBD",
        ),
    ],
)
def test_model_creation(
    title, url, published_at, description, price, expected_published_at, expected_price, expected_price_string
):
    """Models should be created crated correctly"""
    item = SearchItem(title, url, published_at, description, price)

    assert item.title == title, "title was not added to SearchItem"
    assert item.url == url, "url was not added to SearchItem"
    assert item.description == description, "description was not added to SearchItem"

    assert (
        item.published_at == expected_published_at
    ), "published_at was not parsed correctly"
    assert item.price == expected_price, "price is not turned to number correctly"
    assert type(item.price) == float, "price should be float regardless of value"
    assert item.price_str == expected_price_string, "price is not formatted correctly"


def test_model_creation_comparison():
    """The default behaviour for SearchItems is to rang by price"""
    data = [
        [
            "HARRY POTTER",
            "https://www.bolha.com/kocke/harry-potter-oglas-3877893",
            "2020-05-01T20:00:00+02:00",
            "Prodam lego kocke Harry Potter komplet, je odlicno ohranjen!",
            "75\xa0€",
        ],
        [
            "HARRY POTTER",
            "https://www.bolha.com/kocke/harry-potter-oglas-3877893",
            "2020-05-31T20:00:00+02:00",
            "Prodam lego kocke Harry Potter komplet, je odlicno ohranjen!",
            "Cena po dogvoru",
        ]
    ]

    item_1 = SearchItem(*data[0])
    item_2 = SearchItem(*data[1])

    assert item_1 > item_2, "Prices are not parsed correctly"
