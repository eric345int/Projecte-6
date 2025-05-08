
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.




class Sensor:
    def __init__(self, valor_inicial=0):
        self.__valor = valor_inicial

    @property
    def valor(self):
        """Getter per obtenir el valor actual"""
        return self.__valor

    @valor.setter
    def valor(self, valor):
        """Setter per establir el valor (només entre 0 i 100)"""
        if 0 <= valor <= 100:
            self.__valor = valor
        else:
            print("El valor ha de ser entre 0 i 100.")
