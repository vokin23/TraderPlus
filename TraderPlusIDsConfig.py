import json


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    prices = read_json('result/TraderPlusPriceConfig.json')["TraderCategories"]
    generals = read_json('result/TraderPlusGeneralConfig.json')["Traders"]

    ids = []

    for general in generals:
        categories = []
        for price in prices:
            if general["GivenName"] in price["CategoryName"]:
                categories.append(price["CategoryName"])
        data = {
            "Id": general["Id"],
            "Categories": categories,
            "LicencesRequired": [],
            "CurrenciesAccepted": []
        }
        ids.append(data)

    ds = {
        "Version": "2.5",
        "IDs": ids
    }
    write_json('result/TraderPlusIDsConfig.json', ds)