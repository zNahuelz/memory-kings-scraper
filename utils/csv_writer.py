import csv 

def main(products,subsection_name):
    with open(f'{subsection_name}.csv','w',newline='') as file:
        header = ['PRODUCTO','SUBTITULO','DESCRIPCIÓN','NÚMERO DE PARTE','CÓDIGO INTERNO','STOCK','PRECIO USD.','PRECIO SOL','IMAGEN']
        writer = csv.DictWriter(file,fieldnames=header)
        writer.writeheader()
        for i in products:
            writer.writerow({'PRODUCTO':i.title,
                            'SUBTITULO':i.subtitle,
                            'DESCRIPCIÓN':i.description,
                            'NÚMERO DE PARTE':i.part_number,
                            'CÓDIGO INTERNO':i.code,
                            'STOCK':i.stock,
                            'PRECIO USD.':i.price_usd,
                            'PRECIO SOL':i.price_s,
                            'IMAGEN':i.image})

    print(f'[INFO] : Archivo .CSV guardado correctamente. Nombre: {subsection_name}.csv')

if __name__ == "__main__":
    main()