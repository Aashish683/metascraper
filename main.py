import constants as cts
import scraper as spr
import json

# site = cts.Site.META_STUDIO
site = cts.Site.CLIX

if site == cts.Site.META_STUDIO:
    base_url = 'http://doer.metastudio.org/phet/en/simulations.html'
    file_name = 'phetdatametastudio.json'
if site == cts.Site.CLIX:
    base_url = 'https://testing-clix.tiss.edu/softwares/DOER/PhET/en/simulations.html'
    file_name = 'phetdataclix.json'

data = spr.scrape(base_url)

with open(file_name, 'w') as outfile:
    json.dump(data, outfile, indent=2)
