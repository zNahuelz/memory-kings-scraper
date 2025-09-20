from utils.models import Category
from utils.helpers import get_soup
from scrapers import scrape_category
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from typing import List

def get_categories(soup: BeautifulSoup) -> List[Category]:
    box = soup.find('ul', class_="products flex grid-1-4 grid-1-3-m grid-1-2-s grid-1-1-xs pt-2")
    if not box:
        return [] 

    categories = []
    for li in box.find_all('li'):
        anchor = li.find('a')
        title = li.find('h4').get_text(strip=True) if li.find('h4') else "SIN TÍTULO"
        image = li.find('img')['src'] if li.find('img') else ""

        url = urljoin("https://www.memorykings.pe", anchor['href'])
        category = Category(title = title, url = url, image = image, products = [])

        category.products = scrape_category.get_product_list(category)
        categories.append(category)

    return categories

def main(SECTION_URL):
    soup = get_soup(SECTION_URL)
    categories = get_categories(soup)
    return categories