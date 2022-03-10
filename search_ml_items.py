import requests as req
from datetime import datetime


SITE_ID = input("Ingrese el SITE_ID: ").upper()#MLA
SELLER_ID = input("Ingrese el SELLER_ID: ") #179571326
"""
Script para generar un log con los items de un vendedor de Mercadolibre.
Api: http://developers.mercadolibre.com/
"""
def main():
    items = find_items_by_site_and_seller(SITE_ID, SELLER_ID)
    logs = []
    for item in items:
        date = datetime.now()
        item_id = item["id"]
        item_title = item["title"]
        category_id = item["category_id"]
        category = find_category_by_id(category_id)
        category_name = category["name"]
        #2022-03-10 00:10:40.956110 item_id: MLA926000369 item_title: Switch Linksys Se3008 category_id: MLA1708 category_name: Switches
        log = (f'{date} '
              f'item_id: {item_id} '
              f'item_title: {item_title} '
              f'category_id: {category_id} '
              f'category_name: {category_name}\n')
        logs.append(log)
    file_date = datetime.now().strftime('%m-%d-%Y_%H.%M.%S')
    # MLA_179571326_03-10-2022_00.10.50.txt
    with open(f'{SITE_ID}_{SELLER_ID}_{file_date}.txt','w') as f: 
        f.writelines(logs)

def find_items_by_site_and_seller(site_id, seller_id):
    request = req.get(f'https://api.mercadolibre.com//sites/{site_id}/search?seller_id={seller_id}')
    response = request.json()
    items = response["results"]
    return items

def find_category_by_id(category_id):
    request = req.get(f'https://api.mercadolibre.com/categories/{category_id}')
    category = request.json()
    return category

if __name__ == "__main__":
    main()