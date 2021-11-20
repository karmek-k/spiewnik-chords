from typing import List

import bs4
import requests


class Song:
    def __init__(self, song_url: str) -> None:
        self.scrape(get_page(song_url))
    
    def __str__(self) -> str:
        return f'{self.artist} - {self.title}: {" ".join(self.chords)}'
    
    @staticmethod
    def scrape_chords(soup: bs4.BeautifulSoup) -> List[str]:
        """Scrapes and returns chords from the given HTML code."""
        
        chords = []
        for code_tag in soup.find_all('code'):
            chord = f'{code_tag["data-chord"]}{code_tag["data-suffix"]}'
            if code_tag['data-chord'] and chord not in chords:
                chords.append(chord)

        return chords
    
    @staticmethod
    def scrape_title(soup: bs4.BeautifulSoup) -> str:
        """Scrapes and returns song's title."""

        return soup.select_one('h1 strong').text
    
    @staticmethod
    def scrape_artist(soup: bs4.BeautifulSoup) -> str:
        """Scrapes and returns song's artist/author."""

        tag = soup.select_one('h1')
        tag.find('strong').extract()

        return tag.text.strip()
    
    def scrape(self, html: str) -> None:
        soup = bs4.BeautifulSoup(html, 'html.parser')

        self.chords = self.scrape_chords(soup)
        self.title = self.scrape_title(soup)
        self.artist = self.scrape_artist(soup)


def get_page(url: str) -> str:
    """Fetches a page's HTML."""

    res = requests.get(url)

    if res.status_code >= 400:
        raise Exception('Bad status code')

    return res.text


print(Song('https://spiewnik.wywrota.pl/szanty/morskie-opowiesci'))