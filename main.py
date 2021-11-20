from typing import List

import bs4
import requests


def get_page(url: str) -> str:
    """Fetches a page's HTML."""

    res = requests.get(url)

    if res.status_code >= 400:
        raise Exception('Bad status code')

    return res.text


def scrape_chords(html: str) -> List[str]:
    """Scrapes and returns chords from the given HTML code."""
    
    soup = bs4.BeautifulSoup(html, 'html.parser')

    chords = []
    for codeTag in soup.find_all('code'):
        chord = f'{codeTag["data-chord"]}{codeTag["data-suffix"]}'
        if codeTag['data-chord'] and chord not in chords:
            chords.append(chord)

    return chords

html = get_page('https://spiewnik.wywrota.pl/szanty/morskie-opowiesci')

print(scrape_chords(html))
