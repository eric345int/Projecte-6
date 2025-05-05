# 9. Crear el fitxer si no existeix
fitxer_nom = "creacio.txt"
try:
    with open(fitxer_nom, "r", encoding="utf-8") as fitxer:
        print("Contingut del fitxer:")
        print(fitxer.read())
except FileNotFoundError:
    with open(fitxer_nom, "w", encoding="utf-8") as nou_fitxer:
        nou_fitxer.write("Fitxer creat automàticament.\n")
    print(f"El fitxer '{fitxer_nom}' no existia, s'ha creat.")
