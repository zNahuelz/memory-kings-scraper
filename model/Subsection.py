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