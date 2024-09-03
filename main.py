import section_worker as sw
import subsection_worker as ssw
import product_worker as pw
import time
from datetime import datetime

SECTION_URL = "https://www.memorykings.pe/subcategorias/1/accesorios"

def main():
    start_date = datetime.now()
    print("[INFO] Process started at: "+start_date.strftime("%d/%m/%Y %H:%M:%S"))
    start = time.time()
    total_products = 0
    subsections = sw.main(SECTION_URL)


    for i in subsections:
        print('---------------------------------------------------')
        print('SUBSECCIÓN: '+i.title+'\n')
        print('Productos: ')
        for p in i.products:
            total_products += 1
            product = pw.main(p)
            product.print_details()
            print('============================================================================')

    end = time.time()

    elapsed_seconds = end - start
    elapsed_minutes = elapsed_seconds / 60

    print('[INFO] Products Found: '+str(total_products))
    print(f'[INFO] Time: {elapsed_minutes:.4f} minutes')
    now = datetime.now()
    print("[INFO] START TIME: "+start_date.strftime("%d/%m/%Y %H:%M:%S"))
    print("[INFO] END TIME: "+now.strftime("%d/%m/%Y %H:%M:%S"))
if __name__ == "__main__":
    main()