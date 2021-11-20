import requests


def get_page(url: str) -> str:
    """Fetches a page's HTML."""

    res = requests.get(url)

    if res.status_code >= 400:
        raise Exception('Bad status code')

    return res.text
