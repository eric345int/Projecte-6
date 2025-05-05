# 2. Escriure en un fitxer (sobreescriure)
with open("sortida.txt", "w", encoding="utf-8") as fitxer:
    fitxer.write("Primera línia.\n")
    fitxer.write("Segona línia.\n")
    fitxer.write("Tercera línia.\n")
print("Fitxer 'sortida.txt' escrit correctament.")
