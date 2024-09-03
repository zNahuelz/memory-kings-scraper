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