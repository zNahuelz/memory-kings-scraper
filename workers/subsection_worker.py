from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from utils.app_utils import Product
from utils.app_utils import Section
from utils.app_utils import Subsection

def get_soup(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return BeautifulSoup(html,"html.parser")

def get_product_list(section: Section):
    products_urls = []
    page = get_soup(section.url)
    list = page.find('ul', class_="products flex grid-1-4 grid-1-2-m grid-1-1-s pt-2")
    products = list.find_all('li')
    for i in products:
        url = i.find('a')['href']
        products_urls.append('https://www.memorykings.pe'+url)
    return products_urls

def main(section: Section):
    get_product_list(section)

if __name__ == "__main__":
    main()