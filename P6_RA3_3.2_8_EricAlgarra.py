
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular quants punts te un alumne en un examen,sapiguer l'edat i que no hi sigui negativa .

#Especificacions d'entrada:funcio per calcular  quants punts te un alumne en un examen,sapiguer l'edat i que no hi sigui negativa .



class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre):
        return ((self.x - altre.x) ** 2 + (self.y - altre.y) ** 2)

class Alumne:
    def __init__(self, nom, edat_inicial=0):
        self.nom = nom
        self.__edat = edat_inicial

    @property
    def edat(self):
        
        return self.__edat

    @edat.setter
    def edat(self, valor):
        
        if valor >= 0:
            self.__edat = valor
        else:
            print("L'edat no pot ser negativa.")
