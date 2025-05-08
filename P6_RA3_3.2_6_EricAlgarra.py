
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.


class Producte:
    def __init__(self, nom, preu_inicial):
        self.nom = nom
        self.__preu = preu_inicial

    @property
    def preu(self):
        """Getter per obtenir el preu"""
        return self.__preu

    @preu.setter
    def preu(self, valor):
        """Setter per establir el preu (només si és superior a 0)"""
        if valor > 0:
            self.__preu = valor
        else:
            print("El preu ha de ser superior a 0.")
