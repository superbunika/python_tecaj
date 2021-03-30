"""
Zadatak: učitaj dictionary iz json datoteke i ispiši ga formatirano i identirano
u ovisnosti koliko duboko je ugnježđena vrijednost.

Ne očekuje se da će liste imati složene varijable (druge liste ili dictionarije)

1. Učitaj dictionary iz jsona
2. Iteriraj kroz dictionary i ispiši key value parove
3. Ukoliko je item novi dictionary, odi na 2.
"""

import json

with open("podaci.json", encoding="utf8") as f:
    podaci = json.load(f)

def rekurzija(ulaz, prefiks = ""):
    if type(ulaz) is list:
        for v in ulaz:
            if type(v) is dict or type(v) is list:
                rekurzija(v, prefiks + "        ")
            else:
                print("{}{}".format(prefiks, v))
    
    if type(ulaz) is dict:
        for k, v in ulaz.items():
            if type(v) is dict or type(v) is list:
                print("{}{}:".format(prefiks, k))
                rekurzija(v, prefiks + "        ")
            else:
                print("{}{}: {}".format(prefiks, k, v))

rekurzija(podaci)
