import workers.section_worker as section_worker
import workers.subsection_worker as subsection_worker
import workers.product_worker as product_worker
import utils.excel_writer as excel_writer
import utils.csv_writer as csv_writer
import time
from datetime import datetime
import argparse
import json
import sys
import utils.validations as v

"""TODO: 
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
        return 10
    

def execute(args):
    if v.validate_time(int(args.tiempo)):
        start_extraction(args,int(args.extension))
    else:
        print('Tiempo de espera entre extracción de productos mayor a 60 segundos. ¿Desea continuar? (S/N)')
        response = input()
        if v.validate_condition(response) and v.affirmative_condition(response):
            start_extraction(args,int(args.extension))
        else:
            print('Operación cancelada o respuesta invalida. Debe ingresar S ó N')
            exit()


def start_extraction(args,extension):
    START_DATE = datetime.now()
    total_products = 0
    products = []
    print(f'[INFO] : Proceso iniciado el {START_DATE.strftime("%d/%m/%Y %H:%M:%S")}')

    start = time.time()

    if args.seccion != "FULL":
        subsections = section_worker.main(get_section(args.seccion))
        print(f'[INFO] : Extrayendo productos de la sección: {args.seccion}')
        print(f'[INFO] : Tiempo de espera entre productos: {args.tiempo} segundos.')

        for i in subsections:
            i.print_details()
            print('Productos: ')
            for p in i.products:
                total_products += 1
                time.sleep(int(args.tiempo))
                product = product_worker.main(p)
                product.print_details()
                products.append(product)      

        if extension == 0:
            excel_writer.main(products,args.seccion)
        elif extension == 1:
            csv_writer.main(products,args.seccion)
        else:
            excel_writer.main(products,args.seccion)
            csv_writer.main(products,args.seccion)

        end = time.time()

        elapsed_time = (end-start) / 60

        print(f'[INFO] : Productos encontrados: {str(total_products)}')
        print(f'[INFO] : Tiempo transcurrido: {elapsed_time:.4f} minutos.')
        print(f'[INFO] : HORA DE INICIO: {START_DATE.strftime("%d/%m/%Y %H:%M:%S")}')
        print(f'[INFO] : HORA DE FINALIZACIÓN: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')

    else:
        extract_full_site(args,extension)

##TODO....
def extract_full_site(args,extension):
    START_DATE = datetime.now()
    total_products = 0
    products = []
    sections = []
    config = read_config()
    for i in config['sections']:
        sections.append(i.values())
    
    print(f'[INFO] : Proceso iniciado el {START_DATE.strftime("%d/%m/%Y %H:%M:%S")}')

    start = time.time()

    for i in sections:
        subsection = section_worker.main(i)
        print(f'[INFO] : Extrayendo productos de la sección: {args.seccion}')
        print(f'[INFO] : Tiempo de espera entre productos: {args.tiempo} segundos.')
        subsection.print_details()
        print('Productos: ')
        for p in subsection.products:
            total_products += 1
            time.sleep(int(args.tiempo))
            product = product_worker.main(p)
            product.print_details()
            products.append(product)      
    if extension == 0:
        excel_writer.main(products,args.seccion)
    elif extension == 1:
        csv_writer.main(products,args.seccion)
    else:
        excel_writer.main(products,args.seccion)
        csv_writer.main(products,args.seccion)

    end = time.time()

    elapsed_time = (end-start) / 60

    print(f'[INFO] : Productos encontrados: {str(total_products)}')
    print(f'[INFO] : Tiempo transcurrido: {elapsed_time:.4f} minutos.')
    print(f'[INFO] : HORA DE INICIO: {START_DATE.strftime("%d/%m/%Y %H:%M:%S")}')
    print(f'[INFO] : HORA DE FINALIZACIÓN: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')


    
def main():
    parser = argparse.ArgumentParser(prog = 'memory_kings_scrapper',description = 'Web scrapper para el sitio web de MemoryKings Peru.')

    parser.add_argument('-s','--seccion',type=str,help='Nombre de la sección a exportar. Vease el listado de secciones en el archivo config.json',default='SOFTWARE_WIN_OFFICE')
    parser.add_argument('-t','--tiempo',type=v.reject_negatives,help='Tiempo de espera entre obtención de productos. Entre 0 y 60 segundos.',default=0)
    parser.add_argument('-f','--full',type=str,help='Exportar todos los productos de la web en un solo archivo. (S/N)',default='n')
    parser.add_argument('-e','--extension',type=v.reject_negatives,help='Tipo de archivo de destino. 0 -> EXCEL | 1 -> CSV | 2 -> EXCEL y CSV',default=0)

    args = parser.parse_args()

    execute(args)

if __name__== '__main__':
    main()