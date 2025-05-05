# 5. Llegir i escriure
try:
    with open("sortida.txt", "r+", encoding="utf-8") as fitxer:
        contingut = fitxer.read()
        print("Contingut actual del fitxer:")
        print(contingut)
        fitxer.write("Línia afegida amb mode r+.\n")
except FileNotFoundError:
    print("El fitxer no existeix.")
