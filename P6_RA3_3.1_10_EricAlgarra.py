
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.



class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre):
        return ((self.x - altre.x) ** 2 + (self.y - altre.y) ** 2)