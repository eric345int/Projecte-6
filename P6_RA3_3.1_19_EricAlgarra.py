#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.

import math

class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def calcular_area(self):
        return math.pi * self.radi ** 2

    def calcular_perimetre(self):
        return 2 * math.pi * self.radi


cercle1 = Cercle(5)
cercle2 = Cercle(3)
cercle3 = Cercle(8)

cercles = [cercle1, cercle2, cercle3]


for cercle in cercles:
    if cercle.calcular_area() > 50:
        print(f"Cercle amb radi {cercle.radi} té una àrea superior a 50.")
