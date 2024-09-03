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
        print(f'Producto: {self.title}')
        print('Subtitulo: '+self.subtitle)
        print('Número de Parte: '+self.part_number)
        print('Código Interno: '+self.code)
        print('Stock: '+self.stock)
        print('Precio USD: '+str(self.price_usd))
        print('Precio S/: '+str(self.price_s))
        print('Imagen: '+self.image)
        print('Descripción:\n'+self.description)

class Section:
    def __init__(self,title,url,children_number,childs,image):
        self.title = title
        self.url = url
        self.children_number = children_number
        self.childs = childs

    def print_details(self):
        print('---------------------------------------------------')
        print('Sección: '+self.title)
        print('URL: '+self.url)
        print('Cantidad de Subsecciones: '+self.children_number)
        print('Subsecciones: '+self.childs)
        print('---------------------------------------------------')

class Subsection:
    def __init__(self,title,url,image,products):
        self.title = title
        self.url = url
        self.image = image
        self.products = products

    def print_details(self):
        print('---------------------------------------------------')
        print('Subsección: '+self.title)
        print('URL: '+self.url)
        print('Imagen: '+self.image)
        print('Productos: '+str(self.products))
        print('---------------------------------------------------')