from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

# BASE_URL = 'https://phet.colorado.edu/en/simulations'
BASE_URL = 'http://doer.metastudio.org/phet/en/simulations.html'

page = requests.get(BASE_URL)
soup = BeautifulSoup(page.content, 'lxml')

names = soup.select('span.simulation-list-title')
links = soup.select('a.simulation-link')

for tag, link in zip(names, links):
	print('{}: {}'.format(tag.string, link.get('href')))
	print(urljoin(BASE_URL, link.get('href')))
	print()
