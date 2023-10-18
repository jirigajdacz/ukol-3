import json

with open("body.json", mode="r", encoding="utf-8") as soubor:
    jmena = json.load(soubor)

jmeno = input("zadej jméno")
if jmeno == jmena:
    if jmena >= 60:
        print (f"{jmena} pass")
    elif jmena <= 60:
        print (f"{jmena} fail")
else :
    print (f"neplatné jméno")
    

#nedáří se mi vypsat json