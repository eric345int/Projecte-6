nom1 = "Dante"
edat1 = int(input(f" Introdueix l'edat de{nom1}: "))

nom2 = "Gabriel"
edat2 = int(input(f"Introdueix l'edat de {nom2}: "))

if edat1 > edat2:
    print(f"{nom1} és més gran que {nom2}.")
elif edat2 > edat1:
    print(f"{nom2} és més gran que {nom1}.")
else:
    print(f"{nom1} i {nom2} tenen la mateixa edat.")


