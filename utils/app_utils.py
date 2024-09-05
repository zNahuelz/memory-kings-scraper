from urllib.request import urlopen
from bs4 import BeautifulSoup

class Product:
    def __init__(self,title,subtitle,part_number,code,stock,price_usd,price_s,image,description):
        self.title = title
        self.subtitle = subtitle
        self.part_number = part_number
        self.code = code
        self.stock = stock
        self.price_usd = price_usd
        self.price_s = price_s
        self.image = image
        self.description = description

    def print_details(self):
        print('**************************************************')
        print(f'Producto: {self.title}')
        print(f'Subtitulo: {self.subtitle}')
        print(f'Número de Parte: {self.part_number}')
        print(f'Código Interno: {self.code}')
        print(f'Stock: {self.stock}')
        print(f'Precio USD: {str(self.price_usd)}')
        print(f'Precio S/: {str(self.price_s)}')
        print(f'Imagen: {self.image}')
        print(f'Descripción: {self.description}')
        print('**************************************************')

class Section:
    def __init__(self,title,url,children_number,childs,image):
        self.title = title
        self.url = url
        self.children_number = children_number
        self.childs = childs

    def print_details(self):
        print('**************************************************')
        print(f'Sección: {self.title}')
        print(f'URL: {self.url}')
        print(f'Cantidad de Subsecciones: {self.children_number}')
        print(f'Subsecciones: {self.childs}')
        print('**************************************************')

class Subsection:
    def __init__(self,title,url,image,products):
        self.title = title
        self.url = url
        self.image = image
        self.products = products

    def print_details(self):
        print('==================================================')
        print(f'Subsección: {self.title}')
        print(f'URL: {self.url}')
        print(f'Imagen: {self.image}')
        print('==================================================')

def get_soup(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return BeautifulSoup(html,"html.parser")