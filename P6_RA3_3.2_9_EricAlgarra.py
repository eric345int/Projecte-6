
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.

class Joc:
    def __init__(self):
        self.__puntuacio = 0

    def sumar_punts(self, punts):
        """Mètode per sumar punts a la puntuació"""
        if punts > 0:
            self.__puntuacio += punts
        else:
            print("Els punts han de ser positius.")

    def reiniciar_puntuacio(self):
        """Mètode per reiniciar la puntuació"""
        self.__puntuacio = 0

    @property
    def puntuacio(self):
        """Getter per obtenir la puntuació actual"""
        return self.__puntuacio
