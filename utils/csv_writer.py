import csv 
import os
import time
from utils.helpers import safe_filename

def write_csv(category,output_dir="output"):
    os.makedirs(output_dir,exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"{safe_filename(category.title)}_{timestamp}.csv"
    file_path = os.path.join(output_dir,filename)
    header = [
        'PRODUCTO',
        'SUBTITULO',
        'DESCRIPCION',
        'NUMERO DE PARTE',
        'CODIGO INTERNO',
        'STOCK',
        'PRECIO USD',
        'PRECIO SOLES',
        'IMAGEN',
        'LINK'
    ]

    with open(file_path,'w',newline='',encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=header)
        writer.writeheader()
        for p in category.products:
            writer.writerow({
                'PRODUCTO' : p.title,
                'SUBTITULO' : p.subtitle,
                'DESCRIPCION' : p.description,
                'NUMERO DE PARTE' : p.part_number,
                'CODIGO INTERNO' : p.code,
                'STOCK' : p.stock,
                'PRECIO USD' : p.price_usd,
                'PRECIO SOLES' : p.price_pen,
                'IMAGEN' : p.image_url,
                'LINK' : p.url  
            })
    print(f"[INFO] : CSV Guardado: {file_path}")


def export_categories(categories,output_dir="output"):
    if not categories:
        print("[WARN] : Sin categorías para exportar a CSV.")
        return
    if isinstance(categories,list):
        for category in categories:
            write_csv(category,output_dir=output_dir)
    else:
        write_csv(categories,output_dir=output_dir)