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
