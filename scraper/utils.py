from bs4 import BeautifulSoup
import requests


def get_page(url: str) -> str:
    """Fetches a page's HTML."""

    res = requests.get(url)

    if res.status_code >= 400:
        raise Exception('Bad status code')

    return res.text


def make_soup(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, 'html.parser')
