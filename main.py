from scraper.artist import ArtistPage
from scraper.song import Song

page = ArtistPage('https://spiewnik.wywrota.pl/szanty')
for song in page.scrape():
    print(song)