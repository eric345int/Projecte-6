# 7. Gestionar errors d'escriptura
try:
    with open("resultats.txt", "w", encoding="utf-8") as fitxer:
        fitxer.write("Resultats del programa.\n")
        print("S'ha escrit al fitxer correctament.")
except PermissionError:
    print("Error: No tens permisos per escriure en aquest fitxer.")
