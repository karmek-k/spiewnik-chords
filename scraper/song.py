from typing import List
import re

from bs4 import BeautifulSoup

from scraper.utils import get_page, make_soup


class Song:
    def __init__(self, song_url: str) -> None:
        self.url = song_url

        self.scrape(get_page(song_url))
    
    def __str__(self) -> str:
        return f'{self.artist} - {self.title}: {" ".join(self.chords)}'
    
    @staticmethod
    def scrape_chords(soup: BeautifulSoup) -> List[str]:
        """Scrapes and returns chords from the given HTML code."""
        
        chords = []
        for code_tag in soup.find_all('code'):
            chord = f'{code_tag["data-chord"]}{code_tag["data-suffix"]}'
            if code_tag['data-chord'] and chord not in chords:
                chords.append(chord)

        return chords
    
    @staticmethod
    def scrape_title(soup: BeautifulSoup) -> str:
        """Scrapes and returns song's title."""

        return soup.select_one('h1 strong').text
    
    @staticmethod
    def scrape_artist(soup: BeautifulSoup) -> str:
        """Scrapes and returns song's artist/author."""

        tag = soup.select_one('h1')
        tag.find('strong').extract()

        # remove stuff in parentheses
        return re.sub(r'\(.*\)', '', tag.text).strip()
    
    def scrape(self, html: str) -> None:
        soup = make_soup(html)

        self.chords = self.scrape_chords(soup)
        self.title = self.scrape_title(soup)
        self.artist = self.scrape_artist(soup)
