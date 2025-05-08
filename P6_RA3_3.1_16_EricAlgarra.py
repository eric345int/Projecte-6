
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.



import math


class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self, altre_punt):
        distancia = math.sqrt((altre_punt.x - self.x)**2 + (altre_punt.y - self.y)**2)
        return distancia


punt1 = Punt(0, 0)
punt2 = Punt(3, 4)


distancia = punt1.calcular_distancia(punt2)
print(f"La distància entre els punts és: {distancia}")
