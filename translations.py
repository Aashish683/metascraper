import constants as cts
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import json

def get_simulations(soup):
    simulations = []
    simulations_t = []
    rows = soup.select('div.translated-sims tr')

    for i in range(1, len(rows)):
        c1 = rows[i].select('td.name')[0]
        c2 = rows[i].select('td.translated-name')[0]
        simulations.append(str(c1.get_text(strip=True)))
        simulations_t.append(str(c2.get_text(strip=True)))

    return simulations, simulations_t


site = cts.Site.META_STUDIO
# site = cts.Site.CLIX

if site == cts.Site.META_STUDIO:
    base_url = 'http://doer.metastudio.org/phet/en/simulations/translated.html'
    file_name = 'phettranslationsmetastudio.json'
if site == cts.Site.CLIX:
    base_url = 'https://testing-clix.tiss.edu/softwares/DOER/PhET/en/simulations/translated.html'
    file_name = 'phettranslationsclix.json'

page = requests.get(base_url)
soup = BeautifulSoup(page.content, 'lxml')

rows = soup.select('div.translated-sims tr')

data = {}
data['languages'] = []

for i in range(1, len(rows)):
    new_url = urljoin(base_url, rows[i].select('a')[0].get('href'))
    cells = rows[i].select('td')
    new_page = requests.get(new_url)
    new_soup = BeautifulSoup(new_page.content, 'lxml')
    languages = str(cells[0].get_text(strip=True))
    languages_t = str(cells[1].get_text(strip=True))
    simulations, simulations_t = get_simulations(new_soup)
    data['languages'].append({
        'language': languages,
        'language_translated': languages_t,
        'simulations': simulations,
        'simulations_translated': simulations_t
    })
    print('Language:')
    print(languages)
    print('Language (Translated):')
    print(languages_t)
    print('Simulations:')
    print(simulations)
    print('Simulations (Translated):')
    print(simulations_t)
    print()

with open(file_name, 'w') as outfile:
    json.dump(data, outfile, indent=2)
