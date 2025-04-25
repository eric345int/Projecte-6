import math

PI = 3.1416 # Constant
# Les constants són: PI

def calcular_area(radi):
    return PI * radi ** 2
# La part que és una funció és:
# def calcular_area(radi):
#     return PI * radi ** 2

radi = float(input("Introduireix el radi: ")) # Quina línia llegeix dades de l’usuari?
# Les variables són: radi, area

area = calcular_area(radi)
print("L’àrea del cercle és:", area) # Quina línia mostra el resultat?