from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from utils.app_utils import Product
from utils.app_utils import Section
from utils.app_utils import Subsection
from . import subsection_worker as ssw


def get_soup(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return BeautifulSoup(html,"html.parser")

def get_subsections(soup):
    box = soup.find('ul',class_="products flex grid-1-4 grid-1-3-m grid-1-2-s grid-1-1-xs pt-2")
    list_items = box.find_all('li')
    sections = []

    for li in list_items:
        url = li.find('a')
        title = li.find('h4').get_text()
        image = li.find('img')['src']
        subsection = Subsection(title,'https://www.memorykings.pe'+url['href'],image,[])
        products = ssw.get_product_list(subsection)
        
        sections.append(Subsection(title,'https://www.memorykings.pe'+url['href'],image,products))
    return sections

def main(SECTION_URL):
    soup = get_soup(SECTION_URL)
    subsections = get_subsections(soup)
    return subsections

if __name__ == "__main__":
    main()