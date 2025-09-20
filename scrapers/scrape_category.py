import re
from utils.models import Category
from utils.helpers import get_soup 

def get_product_list(category: Category):
    products_urls = []
    page = get_soup(category.url)
    list = page.find('ul', class_="products flex grid-1-4 grid-1-2-m grid-1-1-s pt-2")
    products = list.find_all('li')
    for i in products:
        url = i.find('a')['href']
        products_urls.append('https://www.memorykings.pe'+url)
    return products_urls

def main(category: Category):
    get_product_list(category)