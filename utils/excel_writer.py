import xlsxwriter
import os
from utils.helpers import safe_filename as safe_name

def write_header(worksheet, workbook):
    cell_format = workbook.add_format({'bold': True})
    headers = [
        'PRODUCTO',
        'SUBTITULO',
        'DESCRIPCIÓN',
        'NÚMERO DE PARTE',
        'CÓDIGO INTERNO',
        'STOCK',
        'PRECIO USD.',
        'PRECIO SOLES',
        'IMAGEN',
        'LINK'
    ]
    for col, header in enumerate(headers):
        worksheet.write(0, col, header, cell_format)

def safe_write(worksheet, row, col, value):
    if isinstance(value, (int, float, str)):
        worksheet.write(row, col, value)
    else:
        worksheet.write(row, col, str(value) if value is not None else "")

def write_products(worksheet, products):
    for row, product in enumerate(products, start=1):
        safe_write(worksheet, row, 0, product.title)
        safe_write(worksheet, row, 1, product.subtitle)
        safe_write(worksheet, row, 2, product.description)
        safe_write(worksheet, row, 3, product.part_number)
        safe_write(worksheet, row, 4, product.code)
        safe_write(worksheet, row, 5, product.stock)
        safe_write(worksheet, row, 6, product.price_usd)
        safe_write(worksheet, row, 7, product.price_pen)
        safe_write(worksheet, row, 8, product.image_url)
        safe_write(worksheet, row, 9, product.url)

def get_unique_sheet_name(base_name, used_names, fallback_prefix="HOJA"):
    name = safe_name(base_name)[:31]
    if not name:
        name = fallback_prefix

    original = name
    counter = 1
    while name in used_names or not name:
        suffix = f"_{counter}"
        name = (original[:31 - len(suffix)]) + suffix
        counter += 1
    used_names.add(name)
    return name

def write_excel(categories, filename="output.xlsx"):
    if not categories:
        print("[WARN] : Sin categorías para exportar a Excel.")
        return

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    filepath = os.path.join(output_dir, filename)
    workbook = xlsxwriter.Workbook(filepath)

    used_names = set()
    sheet_index = 1
    any_sheet_created = False

    for category in categories:
        if not hasattr(category, "products") or not category.products:
            print(f"[WARN] : La categoría '{getattr(category, 'title', 'Sin título')}' no tiene productos. Se omitirá.")
            continue

        base_name = category.title if hasattr(category, "title") else f"Sheet{sheet_index}"
        sheet_name = get_unique_sheet_name(base_name, used_names, fallback_prefix=f"Sheet{sheet_index}")
        worksheet = workbook.add_worksheet(sheet_name)
        write_header(worksheet, workbook)
        write_products(worksheet, category.products)
        sheet_index += 1
        any_sheet_created = True

    workbook.close()
    if any_sheet_created:
        print(f"[INFO] : Archivo Excel guardado correctamente. Nombre: {filename}")