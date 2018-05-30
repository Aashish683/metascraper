from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import parser as psr

def scrape(base_url):
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'lxml')

    tags = soup.select('span.simulation-list-title')
    links = soup.select('a.simulation-link')

    data = {}
    data['simulations'] = []

    for tag, link in zip(tags, links):
        new_url = urljoin(base_url, link.get('href'))
        new_page = requests.get(new_url)
        new_soup = BeautifulSoup(new_page.content, 'lxml')
        subjects = psr.get_subjects(new_soup)
        grades = psr.get_grades(new_soup)
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

    return data
