
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.


class Rellotge:
    def __init__(self, hores_inicials=0):
        self.__hores = hores_inicials

    @property
    def hores(self):
        """Getter per obtenir les hores"""
        return self.__hores

    @hores.setter
    def hores(self, valor):
        """Setter per establir les hores (només entre 0 i 23)"""
        if 0 <= valor <= 23:
            self.__hores = valor
        else:
            print("Les hores han de ser entre 0 i 23.")

    def mostrar_hores(self):
        """Mètode per mostrar les hores en format 'HH:00'"""
        return f"{self.__hores:02d}:00"
