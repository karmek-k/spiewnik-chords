from typing import List

from scraper.song import Song
from scraper.utils import get_page, make_soup


class ArtistPage:
    def __init__(self, page_url: str) -> None:
        self.html = get_page(page_url)

    def scrape(self) -> List[Song]:
        soup = make_soup(self.html)

        songs = []
        for list_item in soup.select('.song-list-group li'):
            if list_item.select_one('.icon-lyrics'):
                continue

            song_url = list_item.find_all('a')[0].get('href')

            song = Song(song_url)
            if song.chords:
                # some songs' chords can't be scraped
                songs.append(song)
        
        return songs
