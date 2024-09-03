import xlsxwriter

def main(products,subsection_name):
    row = 1
    col = 0
    workbook = xlsxwriter.Workbook(f'{subsection_name}.xlsx')
    worksheet = workbook.add_worksheet(subsection_name.capitalize())

    write_header(worksheet,workbook)
    for product in products:
        worksheet.write(row,col,product.title)
        worksheet.write(row,col+1,product.subtitle)
        worksheet.write(row,col+2,product.description)
        worksheet.write(row,col+3,product.part_number)
        worksheet.write(row,col+4,product.code)
        worksheet.write(row,col+5,product.stock)
        worksheet.write(row,col+6,product.price_usd)
        worksheet.write(row,col+7,product.price_s)
        worksheet.write(row,col+8,product.image)
        row+=1
    workbook.close()

def write_header(worksheet,workbook):
    cell_format = workbook.add_format({'bold':True})
    row = 0
    col = 0
    header = ['PRODUCTO','SUBTITULO','DESCRIPCIÓN','NÚMERO DE PARTE','CÓDIGO INTERNO','STOCK','PRECIO USD.','PRECIO SOL','IMAGEN']
    for i in header:
        worksheet.write(row,col,i,cell_format)
        col+=1
    print('[INFO] : Columna de archivo Excel impresa.')
    

if __name__ == "__main__":
    main()