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
        html = psr.get_html(new_soup)
        subjects = psr.get_subjects(new_soup)
        grades = psr.get_grades(new_soup)
        keywords = psr.get_keywords(new_soup)
        description = psr.get_desc(new_soup)
        related_sims = psr.get_related_sims(new_soup)
        credits = psr.get_creds(new_soup)
        data['simulations'].append({
            'simulation_link': str(new_url),
            'html_content': html,
            'simulation_name': str(tag.get_text(strip=True)),
            'educational_subjects': subjects,
            'educational_levels': grades,
            'keywords': keywords,
            'description': description,
            'related_sims': related_sims,
            'credits': credits
        })
        print('Link:')
        print(new_url)
        print('HTML Content:')
        print(html)
        print('Name:')
        print(tag.get_text(strip=True))
        print('Subjects:')
        print(subjects)
        print('Grades:')
        print(grades)
        print('Keywords:')
        print(keywords)
        print('Description:')
        print(description)
        print('Related Sims:')
        print(related_sims)
        print('Credits:')
        print(credits)
        print()

    return data
