import requests
from bs4 import BeautifulSoup
from collections import defaultdict

def remove_middle_name(name_arr):
    new_name = [name_arr[0], name_arr[2]]
    return ' '.join(new_name)

def get_participants_dict() -> defaultdict:
    PARTICIPANTS_URL = 'https://sites.uci.edu/explorecsrworkshop/2021-participants/'
    page = requests.get(PARTICIPANTS_URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    elems = soup.find_all("figure", class_= "aligncenter size-large is-resized")

    # 'name' -> ['major', 'school']
    students = defaultdict(list)
    schools = ['UC Irvine', 'UC Davis', 'University of Southern California', 'Pasadena City College', 'Northeastern University', 'UCLA', 'El Camino College']

    for ele in elems:
        tags = ele.find("figcaption")
        names = tags.find("strong")
        # major = ele.find_all(string = lambda text: 'engineer' in text.lower() or 'science' in text.lower() or 'math' in text.lower() or 'cyber' in text.lower() or 'information' in text.lower() and 'university' not in text.lower())

        name = names.text.strip()
        not_name = tags.text.replace(name, '')

        for school in schools:
            if school in not_name:
                if name.startswith('Chowdhury'):
                    name = 'Chowdhury Mahjabin'
                elif len(name.split()) > 2:
                    name = remove_middle_name(name.split())

                students[name].append(school)
                major = not_name.replace(school, '').strip()
                if major:
                    students[name].append(major)
                else:
                    students[name].append('')
    return dict(students)