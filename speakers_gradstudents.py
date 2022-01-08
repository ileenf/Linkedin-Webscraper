import requests
from bs4 import BeautifulSoup

def remove_middle_name(name_arr):
    new_name = [name_arr[0], name_arr[2]]
    return ' '.join(new_name)

def get_speakers_list(url) -> list:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    elems = soup.find_all("figure", class_= "aligncenter size-large is-resized")

    people = []

    for ele in elems:
        tags = ele.find("figcaption")
        names = tags.find("strong")

        name = names.text.strip()
        if len(name.split()) > 2:
            name = remove_middle_name(name.split())

        people.append(name)


    return people

