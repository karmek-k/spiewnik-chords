import requests


url = 'https://spiewnik.wywrota.pl/szanty/morskie-opowiesci'
res = requests.get(url)

status = res.status_code

if status >= 400:
    print(f'Bad status code: {status}')
    exit(1)
