import bs4
import requests


url = 'https://spiewnik.wywrota.pl/szanty/morskie-opowiesci'
res = requests.get(url)

status = res.status_code

if status >= 400:
    print(f'Bad status code: {status}')
    exit(1)

soup = bs4.BeautifulSoup(res.text, 'html.parser')

chords = []
for codeTag in soup.find_all('code'):
    chord = f'{codeTag["data-chord"]}{codeTag["data-suffix"]}'
    if codeTag['data-chord'] and chord not in chords:
        chords.append(chord)

print(chords)
