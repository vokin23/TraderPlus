import json


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    trader_categories_trader_plus = []

    xzone_traders = read_json('XzoneTrader/XZoneTraderStock.json')['Traders']

    for trader in xzone_traders:
        trader_categories = trader['TraderStocks']
        trader_name = trader["TraderName"]
        for categorie in trader_categories:
            categorie_name = categorie['TraderCaregory']
            categorie_products = categorie["Products"]
            products = []
            for product in categorie_products:
                product_name = product["Classname"]
                purchase_price = product["PurchasePrice"]
                selling_price = product["SellingPrice"]
                products.append(f'{product_name},1,-1,1,{purchase_price},{selling_price}')
            data = {
                "CategoryName": f"{categorie_name} {trader_name}",
                "Products": products
            }
            trader_categories_trader_plus.append(data)
    trader_plus_json = {
        "Version": "2.5",
        "EnableAutoCalculation": 0,
        "EnableAutoDestockAtRestart": 0,
        "EnableDefaultTraderStock": 0,
        "TraderCategories": trader_categories_trader_plus
    }

    write_json('result/TraderPlusPriceConfig.json', trader_plus_json)
