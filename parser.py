from bs4 import BeautifulSoup

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

def get_keywords(soup):
    # tags = soup.select('div#about span[itemprop="keywords"]')
    tags = soup.select('td.simulation-main-description span[itemprop="keywords"]')
    keywords = [str(tag.string) for tag in tags]
    return keywords

def get_desc(soup):
    tags = soup.select('div#about p[itemprop="description about"]')
    return str(tags[0].string)

def get_related_sims(soup):
    tags = soup.select('div#related-sims span.simulation-list-title')
    related_sims = [str(tag.string) for tag in tags]
    return related_sims

def get_creds(soup):
    tags = soup.select('div#credits span')
    credits = [str(tag.string) for tag in tags]
    return credits
