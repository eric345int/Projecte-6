
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer la temperatura d'un termostat i fer que hi sigui entre 10 i 30 graus celcius.

#Especificacions d'entrada:funcio per a sapiguer la temperatura d'un termostat i fer que hi sigui entre 10 i 30 graus celcius.


class Termostat:
    def __init__(self, temperatura_inicial=20):
        self.__temperatura = temperatura_inicial

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if 10 <= valor <= 30:
            self.__temperatura = valor
        else:
            print("La temperatura ha de ser entre 10 i 30 °C.")
