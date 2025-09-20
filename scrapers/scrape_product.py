import re
from utils.models import Product
from utils.helpers import get_soup 
from bs4 import BeautifulSoup

def get_product_title(soup: BeautifulSoup) -> str:
    tag = soup.find('h1')
    return tag.get_text(strip=True) if tag else ""

def get_product_subtitle(soup: BeautifulSoup) -> str:
    tag = soup.find('p', class_="verde")
    return tag.get_text(strip=True) if tag else ""

def get_product_info(soup: BeautifulSoup):
    return soup.find('div', class_="border-card-3 gutter-2 pt-2 pb-2")

def get_product_part_number(product_info) -> str:
    box = product_info.find('div', class_="col-3-4") if product_info else None
    if not box:
        return ""
    text = box.find('div', class_="body-text")
    return text.get_text().split(": ")[1] if text else ""

def get_product_code(product_info) -> str:
    if not product_info:
        return ""
    box = product_info.find('div', class_="col-3-4")
    if not box:
        return ""
    elem = box.find(string=re.compile("Código"))
    if elem:
        sibling = elem.find_next_sibling()
        return sibling.get_text().strip() if sibling else ""
    return ""
    
def get_product_stock(product_info) -> int:
    if not product_info:
        return 0
    box = product_info.find('div', class_="col-3-4")
    if not box:
        return 0
    elem = box.find(string=re.compile("Stock"))
    if elem:
        sibling = elem.find_next_sibling()
        if sibling:
            try:
                return int(sibling.get_text().strip())
            except ValueError:
                return 0
    return 0

def get_product_price(soup: BeautifulSoup,symbol: str) -> float:
    price = soup.find('div', class_="price pt-1")
    if not price:
        return 0.0
    match = re.search(fr'{re.escape(symbol)}\s*([\d,]+(?:\.\d{{2}})?)', price.get_text())
    if match:
        return float(match.group(1).replace(',', ''))
    return 0.0

def get_product_price_usd(soup: BeautifulSoup) -> float:
    return get_product_price(soup, "$")

def get_product_price_pen(soup: BeautifulSoup) -> float:
    return get_product_price(soup, "S/")

def get_product_image(soup: BeautifulSoup,title) -> str:
    image = soup.find('img',alt=title)
    return image['src'] if image and 'src' in image.attrs else ""

def get_product_description(soup: BeautifulSoup) -> str:
    desc = soup.find('div', class_="descripcion-content").get_text()
    return ' '.join(desc.split()) 

def get_product(product_url: str) -> Product:
    soup = get_soup(product_url)
    product_info = get_product_info(soup)

    title = get_product_title(soup)
    return Product(
        title = title,
        subtitle = get_product_subtitle(soup),
        part_number = get_product_part_number(product_info),
        code = get_product_code(product_info),
        stock = get_product_stock(product_info),
        price_usd = get_product_price_usd(soup),
        price_pen = get_product_price_pen(soup),
        image_url = get_product_image(soup,title),
        description = get_product_description(soup),
        url = product_url
    )

def main(url):
    return get_product(url)