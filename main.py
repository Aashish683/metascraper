from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import json

def get_subjects(soup):
    subjects = []
    sub_ids = ['nav-location-nav-physics', 'nav-location-nav-biology',\
               'nav-location-nav-chemistry', 'nav-location-nav-earth-science',\
               'nav-location-nav-math']
    for sub_id in sub_ids:
        tags = soup.select('a#' + sub_id + ' span.selected')
        for tag in tags:
            subjects.append(str(tag.string))
    return subjects

def get_grades(soup):
    grades = []
    grade_ids = ['nav-location-nav-elementary-school', 'nav-location-nav-middle-school',\
                 'nav-location-nav-high-school', 'nav-location-nav-university']
    for grade_id in grade_ids:
        tags = soup.select('a#' + grade_id + ' span.selected')
        for tag in tags:
            grades.append(str(tag.string))
    return grades

# BASE_URL = 'https://phet.colorado.edu/en/simulations'
BASE_URL = 'http://doer.metastudio.org/phet/en/simulations.html'

page = requests.get(BASE_URL)
soup = BeautifulSoup(page.content, 'lxml')

tags = soup.select('span.simulation-list-title')
links = soup.select('a.simulation-link')

data = {}
data['simulations'] = []

for tag, link in zip(tags, links):
    new_url = urljoin(BASE_URL, link.get('href'))
    new_page = requests.get(new_url)
    new_soup = BeautifulSoup(new_page.content, 'lxml')
    subjects = get_subjects(new_soup)
    grades = get_grades(new_soup)
    data['simulations'].append({
        'simulation_link': str(new_url),
        'simulation_name': str(tag.string),
        'educational_subjects': subjects,
        'educational_levels': grades
    })
    print(new_url)
    print(tag.string)
    print(subjects)
    print(grades)
    print()

with open('phetdata.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
