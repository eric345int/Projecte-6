# 4. Comptar línies
try:
    with open("sortida.txt", "r", encoding="utf-8") as fitxer:
        linies = fitxer.readlines()
        print(f"El fitxer té {len(linies)} línies.")
except FileNotFoundError:
    print("El fitxer no existeix.")
