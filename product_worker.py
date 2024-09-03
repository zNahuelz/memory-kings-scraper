from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from model.Product import Product
"""
.-_.-.
TODO: Make the input to be a section url. Then the scrapper must get all the subsections and finally get every product from them.
"""

PRODUCT_LIST = [
    'https://www.memorykings.pe/producto/328122/procesador-intel-cel-g5905-3-5ghz-4mb-1200',
    'https://www.memorykings.pe/producto/329566/procesador-intel-core-i3-10105-3-7ghz-6mb-1200',
    'https://www.memorykings.pe/producto/328729/procesador-intel-core-i3-10105f-3-7ghz-6mb-1200',
    'https://www.memorykings.pe/producto/326672/procesador-intel-core-i5-10400-2-9ghz-12mb-1200',
    'https://www.memorykings.pe/producto/327831/procesador-intel-core-i5-10400f-2-9ghz-12mb-1200',
    'https://www.memorykings.pe/producto/350161/procesador-amd-ryzen-5-8400f-4-7ghz-16mb-6c-am5',
    'https://www.memorykings.pe/producto/349387/procesador-amd-ryzen-5-8500g-3-5ghz-16mb-6c-am5',
    'https://www.memorykings.pe/producto/349388/procesador-amd-ryzen-5-8600g-4-3ghz-16mb-6c-am5',
    'https://www.memorykings.pe/producto/350163/procesador-amd-ryzen-7-8700f-4-1ghz-16mb-8c-am5',
    'https://www.memorykings.pe/producto/349389/procesador-amd-ryzen-7-8700g-4-2ghz-16mb-8c-am5'
]

def get_soup(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return BeautifulSoup(html,"html.parser")

def get_product_title(soup):
    return soup.find('h1').get_text()

def get_product_subtitle(soup):
    try:
        return soup.find('p', class_="verde").get_text()
    except:
        return ''

def get_product_info(soup):
    return soup.find('div', class_="border-card-3 gutter-2 pt-2 pb-2")

def get_product_part_number(product_info):
    box = product_info.find('div', class_="col-3-4")
    part_number = box.find('div', class_="body-text").get_text()
    return part_number.split(": ")[1]

def get_product_code(product_info):
    box = product_info.find('div', class_="col-3-4")
    code = box.find(string=re.compile("Código")).find_next_sibling().get_text()
    return code
    
def get_product_stock(product_info):
    box = product_info.find('div', class_="col-3-4")
    stock = box.find(string=re.compile("Stock")).find_next_sibling().get_text()
    return stock

def get_product_price_usd(soup):
    price = soup.find('div', class_="price pt-1").get_text()
    match = re.search(r'\$ ([\d,]+(\.\d{2})?)', price)
    if match:
        usd_price = match.group(1)
        # Remove commas from the price string and convert to float
        return float(usd_price.replace(',', ''))
    return 0.0

def get_product_price_s(soup):
    price = soup.find('div', class_="price pt-1").get_text()
    match = re.search(r'S/ ([\d,]+(\.\d{2})?)', price)
    if match:
        s_price = match.group(1)
        # Remove commas from the price string and convert to float
        return float(s_price.replace(',', ''))
    return 0.0

def get_product_image(soup,title):
    image = soup.find('img', alt=title)
    return image['src']

def get_product_description(soup):
    desc = soup.find('div', class_="descripcion-content").get_text()
    return ' '.join(desc.split()) 


def get_product(product_url):
    soup = get_soup(product_url)
    title = get_product_title(soup)
    subtitle = get_product_subtitle(soup)
    product_info = get_product_info(soup)
    part_number = get_product_part_number(product_info)
    code = get_product_code(product_info)
    stock = get_product_stock(product_info)
    price_usd = get_product_price_usd(soup)
    price_s = get_product_price_s(soup)
    image = get_product_image(soup,title)
    description = get_product_description(soup)
    return Product(title,subtitle,part_number,code,stock,price_usd,price_s,image,description)


def main(url):
    return get_product(url)

if __name__ == "__main__":
    main()