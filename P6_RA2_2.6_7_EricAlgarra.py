# 6. Comprovar si existeix abans de llegir
import os

nom_fitxer = "dades.txt"
if os.path.exists(nom_fitxer):
    with open(nom_fitxer, "r", encoding="utf-8") as fitxer:
        print("Contingut del fitxer 'dades.txt':")
        print(fitxer.read())
else:
    print(f"El fitxer '{nom_fitxer}' no existeix.")
