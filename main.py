import workers.section_worker as sw
import workers.subsection_worker as ssw
import workers.product_worker as pw
import utils.excel_writer as ew
import time
from datetime import datetime
import argparse
import json
import sys

"""TODO: 
*Añadir tiempo de espera entre obtención de productos.
*Permitir exportar TODA la web, con tiempo de espera entre productos.
*Cada seccion de la web en un archivo distinto & en un mismo archivo, distintas pestañas.
*Permitir exportar TODOS los productos en un mismo archivo excel.
*Refactorizar lo que haga falta.
"""

def get_version():
    try:
        version = read_config()['version']
        print(f'Version: {str(get_version())} Fuente: https://github.com/zNahuelz')
    except:
        return '---'
    
def read_config():
    try:
        with open('config.json','r') as file:
            return json.load(file)
    except FileNotFoundError:
        print('[ERROR] : Archivo de configuración no encontrado.')
    except:
        return {}
    
def get_section(name):
    try:
        config = read_config()
        return config['sections'].get(name)
    except:
        return ''

def get_wait_time():
    try:
        return read_config()['wait_time']
    except:
        return 30
    

def execute(args):
    START_DATE = datetime.now()
    print(f'[INFO] : Proceso iniciado el {START_DATE.strftime("%d/%m/%Y %H:%M:%S")}')
    start = time.time()

    total_products = 0
    products = []
    if args.seccion != "FULL":
        subsections = sw.main(get_section(args.seccion))

        for i in subsections:
            print('---------------------------------------------------')
            print('SUBSECCIÓN: '+i.title+'\n')
            print('Productos: ')
            for p in i.products:
                total_products += 1
                product = pw.main(p)
                product.print_details()
                products.append(product)
                print('============================================================================')

        ew.main(products,args.seccion)
        end = time.time()

        elapsed_time = (end-start) / 60

        print(f'[INFO] : Productos encontrados: {str(total_products)}')
        print(f'[INFO] : Tiempo transcurrido: {elapsed_time:.4f} minutos.')
        print(f'[INFO] HORA DE INICIO: {START_DATE.strftime("%d/%m/%Y %H:%M:%S")}')
        print(f'[INFO] : HORA DE FINALIZACIÓN: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    
def main():
    parser = argparse.ArgumentParser(prog = 'memory_kings_scrapper',description = 'Web scrapper para el sitio web de MemoryKings Peru.')

    parser.add_argument('-s','--seccion',type=str,help='Nombre de la sección a exportar. Vease el listado de secciones en el archivo config.json',default='ACCESORIOS')
    parser.add_argument('-t','--tiempo',type=int,help='Tiempo de espera entre obtención de productos. Vease wait_time en el archivo config.json',default=30)

    args = parser.parse_args()
    if len(sys.argv) < 1:
        parser.print_help()
        exit(0) ##TODO.
    execute(args)
        

if __name__== '__main__':
    main()