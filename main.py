import argparse
import json
import sys
import time
import scrapers.scrape_product as scrape_product
import scrapers.scrape_section as scrape_section
import scrapers.scrape_category as scrape_category
import scrapers.export_sections as export_sections
import utils.excel_writer as excel_writer
import utils.csv_writer as csv_writer
from datetime import datetime
from utils import validations
from utils.helpers import logo
from utils.helpers import get_info
from utils.helpers import read_sections_file
from utils.helpers import get_section

def execute(args):
    if(args.refresh_sections):
        export_sections.main()
        exit()
    
    if validations.validate_time(int(args.time)):
        print(logo())
        start_extraction(args,int(args.extension))
    else:
        print('Tiempo de espera entre extracción de productos mayor a 60 segundos. ¿Desea continuar? (S/N)')
        response = input()
        if validations.validate_condition(response.upper()) and validations.affirmative_condition(response):
            start_extraction(args,int(args.extension))
        else:
            print('Operación cancelada o respuesta invalida. Debe ingresar S ó N')
            exit()


def start_extraction(args, extension):
    START_DATE = datetime.now()
    total_products = 0
    all_products = []  
    print(f'[INFO] : Proceso iniciado el {START_DATE.strftime("%d/%m/%Y %H:%M:%S")}')
    start = time.time()

    if args.full and args.full.upper() == "S":
        config = read_sections_file()
        section_names = list(config.get("sections",{}).keys())
        print(f"[WARN] : Extrayendo TODAS las secciones ({len(section_names)}) definidas en /data/sections.json - Este proceso es tardio.")
    else:
        if not args.section:
            print(f"[ERROR] : Debe especificar al menos una sección con la opción -s o usar -f S para todas las secciones.")
            return
        section_names = [name.strip() for name in args.section.split(",")]

    all_categories = []

    for section_name in section_names:
        section_config = get_section(section_name)
        if not section_config:
            print(f"[WARN] : Sección '{section_name}' no encontrada en /data/sections.json - Se recomienda ejecutar la herramienta con la opción -rs para refrescar el listado de secciones. Puede visualizar la ayuda con --help")
            continue

        categories = scrape_section.main(section_config)
        print(f'[INFO] : Extrayendo productos de la sección: {section_name}')
        print(f'[INFO] : Tiempo de espera entre productos: {args.time} segundos.')

        for category in categories:
            print(f"[INFO] Procesando categoría: {category.title}")
            new_products = []

            for p in category.products:
                total_products += 1
                time.sleep(int(args.time))

                product = scrape_product.main(p)
                print(product)

                new_products.append(product)
                all_products.append(product) 

            category.products = new_products
            all_categories.append(category) 

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    if extension == 0:
        excel_writer.write_excel(all_categories, filename=f"export_{timestamp}.xlsx")
    elif extension == 1:
        csv_writer.export_categories(all_categories)
    else:
        excel_writer.write_excel(all_categories, filename=f"export_{timestamp}.xlsx")
        csv_writer.export_categories(all_categories)

    end = time.time()
    elapsed_time = (end - start) / 60
    print(f'[INFO] : Productos encontrados: {total_products}')
    print(f'[INFO] : Tiempo transcurrido: {elapsed_time:.4f} minutos.')
    print(f'[INFO] : HORA DE INICIO: {START_DATE.strftime("%d/%m/%Y %H:%M:%S")}')
    print(f'[INFO] : HORA DE FINALIZACIÓN: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')

def main():
    parser = argparse.ArgumentParser(prog = "memory_kings_scraper",description = f"{get_info()} \n Web Scraper para el sitio web de MemoryKings Perú.",formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-s','--section',type=str,help='Nombre de las secciones a exportar separadas por comas (,). Vease el listado de secciones en el archivo /data/sections.json',default='SOFTWARE_MICROSOFT_WINDOWS_OFFICE')
    parser.add_argument('-t','--time',type=validations.reject_negatives,help='Tiempo de espera entre solicitudes. Entre 0 y 60 segundos.',default=0)
    parser.add_argument('-f','--full',type=str,help='Exportar toda la web. (S/N)',default='N')
    parser.add_argument('-e','--extension',type=validations.reject_negatives,help='Tipo de archivo de destino. 0 = EXCEL // 1 = CSV // 2 = EXCEL y CSV',default=0)
    parser.add_argument('-rs','--refresh-sections',help='Refresca las secciones de la web. Son guardadas en /data/sections.json para su posterior uso.',action="store_true")

    args = parser.parse_args()
    execute(args)

if __name__== '__main__':
    main()
