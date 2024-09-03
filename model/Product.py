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
        print('Producto: '+self.title)
        print('Subtitulo: '+self.subtitle)
        print('Número de Parte: '+self.part_number)
        print('Código Interno: '+self.code)
        print('Stock: '+self.stock)
        print('Precio USD: '+str(self.price_usd))
        print('Precio S/: '+str(self.price_s))
        print('Imagen: '+self.image)
        print('Descripción:\n'+self.description)