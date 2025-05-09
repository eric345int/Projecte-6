
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a  definir el que ha de tindre un videojoc com els punts totals que hi siguin positiusi els punts totals.

#Especificacions d'entrada:funcio per a  definir el que ha de tindre un videojoc com els punts totals que hi siguin positiusi els punts totals.

class Joc:
    def __init__(self):
        self.__puntuacio = 0
    def sumar_punts(self, punts):
        if punts > 0:
            self.__puntuacio += punts
        else:
            print("Els punts han de ser positius.")
    def reiniciar_puntuacio(self):
        self.__puntuacio = 0

    @property
    def puntuacio(self):
        return self.__puntuacio
