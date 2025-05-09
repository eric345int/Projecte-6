
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer el nom d'un producte,el preu inicial establir el preu,i que el preu ha de ser superior a 0.

#Especificacions d'entrada:funcio per a sapiguer el nom d'un producte,el preu inicial establir el preu,i que el preu ha de ser superior a 0.


class Producte:
    def __init__(self, nom, preu_inicial):
        self.nom = nom
        self.__preu = preu_inicial

    @property
    def preu(self):
        return self.__preu

    @preu.setter
    def preu(self, valor):
        if valor > 0:
            self.__preu = valor
        else:
            print("El preu ha de ser superior a 0.")
