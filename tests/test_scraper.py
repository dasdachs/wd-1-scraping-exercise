from pathlib import Path

import pytest
import requests

from src.scraper import prepare_url, extract_content_from_html, search


@pytest.fixture()
def get_html():
    """Returns a striped down html response for search pattern Harry Potter"""
    with open(Path("tests", "test_data", "bolha_harry_potter.html")) as html_file:
        html = html_file.read()

    return html


@pytest.mark.parametrize(
    ("search_input", "url"),
    [
        ("kolo", "https://www.bolha.com/?ctl=search_ads&keywords=kolo"),
        ("nov avto", "https://www.bolha.com/?ctl=search_ads&keywords=nov+avto"),
        (
            "hiša slovenska obala",
            "https://www.bolha.com/?ctl=search_ads&keywords=hiša+slovenska+obala",
        ),
        ("", "https://www.bolha.com/?ctl=search_ads&keywords="),
    ],
)
def test_prepare_url(search_input, url):
    """URL has to include the corrected formatted text"""
    assert prepare_url(search_input) == url


def test_extract_content_from_html(get_html):
    """Content should return only the needed data"""
    expected = [
        {
            "title": "KUPIM: Harry Potter CELO ZBIRKO",
            "url": "https://www.bolha.com/knjizne-zbirke/kupim-harry-potter-celo-zbirko-oglas-3882387",
            "description": "KUPIM: Harry Potter CELO ZBIRKO",
            "published_at": "2020-05-27T14:34:07+02:00",
            "price": "Cena po dogovoru",
        },
        {
            "title": "Originalne PCCD ROM igre HARRY POTTER",
            "url": "https://www.bolha.com/vhs-komponente/originalne-pc-cd-rom-igre-harry-potter-oglas-3781330",
            "description": "Originalne PCCD ROM igre HARRY POTTER",
            "published_at": "2020-05-07T11:50:43+02:00",
            "price": "Cena po dogovoru",
        },
        {
            "title": "HARRY POTTER",
            "url": "https://www.bolha.com/kocke/harry-potter-oglas-3877893",
            "description": "Prodam lego kocke Harry Potter komplet, je odlicno ohranjen!",
            "published_at": "2020-05-26T15:11:27+02:00",
            "price": "75\xa0€",
        },
    ]

    assert extract_content_from_html(get_html) == expected


def test_search(monkeypatch):
    """Final test, tie it all together"""

    class MockResponse:
        text = open(Path("tests", "test_data", "bolha_harry_potter.html")).read()

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    expected = [
        {
            "title": "KUPIM: Harry Potter CELO ZBIRKO",
            "url": "https://www.bolha.com/knjizne-zbirke/kupim-harry-potter-celo-zbirko-oglas-3882387",
            "description": "KUPIM: Harry Potter CELO ZBIRKO",
            "published_at": "2020-05-27T14:34:07+02:00",
            "price": "Cena po dogovoru",
        },
        {
            "title": "Originalne PCCD ROM igre HARRY POTTER",
            "url": "https://www.bolha.com/vhs-komponente/originalne-pc-cd-rom-igre-harry-potter-oglas-3781330",
            "description": "Originalne PCCD ROM igre HARRY POTTER",
            "published_at": "2020-05-07T11:50:43+02:00",
            "price": "Cena po dogovoru",
        },
        {
            "title": "HARRY POTTER",
            "url": "https://www.bolha.com/kocke/harry-potter-oglas-3877893",
            "description": "Prodam lego kocke Harry Potter komplet, je odlicno ohranjen!",
            "published_at": "2020-05-26T15:11:27+02:00",
            "price": "75\xa0€",
        },
    ]

    assert search("harry potter") == expected
