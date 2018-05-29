from bs4 import BeautifulSoup
import requests

# BASE_URL = 'https://phet.colorado.edu/en/simulations'
BASE_URL = 'http://doer.metastudio.org/phet/en/simulations.html'

page = requests.get(BASE_URL)
soup = BeautifulSoup(page.content, 'lxml')

for tag in soup.select('span.simulation-list-title'):
	print(tag.get_text())
