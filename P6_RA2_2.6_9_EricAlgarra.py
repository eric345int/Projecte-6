# 8. Evitar bloqueig per fitxer mal format
try:
    with open("nombres.txt", "r", encoding="utf-8") as fitxer:
        for i, linia in enumerate(fitxer, 1):
            try:
                nombre = int(linia.strip())
                print(f"Línia {i}: {nombre}")
            except ValueError:
                print(f"Línia {i}: No és un enter vàlid: '{linia.strip()}'")
except FileNotFoundError:
    print("El fitxer 'nombres.txt' no existeix.")
