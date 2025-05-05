# Llegir i mostrar el contingut de missatge.txt
try:
    with open("missatge.txt", "r", encoding="utf-8") as fitxer:
        contingut = fitxer.read()
        print("Contingut del fitxer:")
        print(contingut)
except FileNotFoundError:
    print("El fitxer 'missatge.txt' no existeix.")
