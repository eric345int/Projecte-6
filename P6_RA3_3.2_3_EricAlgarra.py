
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.


class Termostat:
    def __init__(self, temperatura_inicial=20):
        self.__temperatura = temperatura_inicial

    @property
    def temperatura(self):
        """Getter per obtenir la temperatura actual"""
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        """Setter per establir la temperatura (només entre 10 i 30 °C)"""
        if 10 <= valor <= 30:
            self.__temperatura = valor
        else:
            print("La temperatura ha de ser entre 10 i 30 °C.")
