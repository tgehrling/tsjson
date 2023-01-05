import json
with open("tsjson/accounts.json") as json_datei:
    print(type(json_datei))
    python_liste = json.load(json_datei)
    print(python_liste)
