import json


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    traders_trader_plus = []

    xzone_traders = read_json('XzoneTrader/XZoneTraderStock.json')['Traders']

    for i, trader in enumerate(xzone_traders):
        trader_categories = trader['TraderStocks']
        trader_name = trader["TraderName"]
        positions = trader["PositionsSpawnMain"]
        orientation = trader["OrientationSpawnMain"]
        class_name = trader["TraderType"]
        data = {
            "Id": i,
            "Name": class_name,
            "GivenName": trader_name,
            "Role": "Trader",
            "Position": positions,
            "Orientation": orientation,
            "Clothes": []
        }
        traders_trader_plus.append(data)

    trader_plus_json = {
        "Version": "2.5",
        "ConvertTraderConfigToTraderPlus": 0,
        "ConvertTraderConfigToTraderPlusWithStockBasedOnCE": 0,
        "UseGarageToTradeCar": 1,
        "DisableHeightFailSafeForReceiptDeployment": 0,
        "HideInsuranceBtn": 0,
        "HideGarageBtn": 0,
        "HideLicenceBtn": 0,
        "EnableShowAllPrices": 0,
        "EnableShowAllCheckBox": 1,
        "IsReceiptTraderOnly": 1,
        "IsReceiptSaveLock": 0,
        "IsReceiptSaveAttachment": 0,
        "IsReceiptSaveCargo": 0,
        "LockPickChance": 0.30000001192092898,
        "LicenceKeyWord": "Licence",
        "Licences": [
            "Car Licence",
            "Admin Licence"
        ],
        "AcceptedStates": {
            "AcceptWorn": 1,
            "AcceptDamaged": 1,
            "AcceptBadlyDamaged": 1,
            "CoefficientWorn": 0.75,
            "CoefficientDamaged": 0.5,
            "CoefficientBadlyDamaged": 0.25
        },
        "StoreOnlyToPristineState": 0,
        "Currencies": [
            {
                "ClassName": "TraderPlus_Money_Ruble5000",
                "Value": 5000
            },
            {
                "ClassName": "TraderPlus_Money_Ruble2000",
                "Value": 2000
            },
            {
                "ClassName": "TraderPlus_Money_Ruble1000",
                "Value": 1000
            },
            {
                "ClassName": "TraderPlus_Money_Ruble500,TraderPlus_Money_Euro500",
                "Value": 500
            },
            {
                "ClassName": "TraderPlus_Money_Ruble200,TraderPlus_Money_Euro200",
                "Value": 200
            },
            {
                "ClassName": "TraderPlus_Money_Ruble100,TraderPlus_Money_Euro100,TraderPlus_Money_Dollar100",
                "Value": 100
            },
            {
                "ClassName": "TraderPlus_Money_Ruble50,TraderPlus_Money_Euro50,TraderPlus_Money_Dollar50",
                "Value": 50
            },
            {
                "ClassName": "TraderPlus_Money_Ruble10,TraderPlus_Money_Euro10,TraderPlus_Money_Dollar10",
                "Value": 10
            },
            {
                "ClassName": "TraderPlus_Money_Ruble5,TraderPlus_Money_Euro5,TraderPlus_Money_Dollar5",
                "Value": 5
            },
            {
                "ClassName": "TraderPlus_Money_Ruble2_Coin,TraderPlus_Money_Euro2,TraderPlus_Money_Dollar2",
                "Value": 2
            },
            {
                "ClassName": "TraderPlus_Money_Ruble1_Coin,TraderPlus_Money_Euro1,TraderPlus_Money_Dollar1",
                "Value": 1
            }
        ],
        "Traders": traders_trader_plus
    }

    write_json('result/TraderPlusGeneralConfig.json', trader_plus_json)
