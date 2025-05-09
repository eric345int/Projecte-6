

#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer de una figura l'area, del quadrat un costat i l'area i de un cercle el radi i l'area.

#Especificacions d'entrada:funcio  per a sapiguer de una figura l'area, del quadrat un costat i l'area i de un cercle el radi i l'area. .


import math

class Figura:
    def area(self):
        print("Àrea no definida")

class Quadrat(Figura):
    def __init__(self, costat):
        self.costat = costat

    def area(self):
        return self.costat ** 2

class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * self.radi ** 2


