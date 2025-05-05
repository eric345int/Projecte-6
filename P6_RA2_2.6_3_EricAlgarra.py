# 3. Afegir continguts
with open("sortida.txt", "a", encoding="utf-8") as fitxer:
    fitxer.write("Aquesta línia s'ha afegit al final.\n")
print("Línia afegida a 'sortida.txt'.")
