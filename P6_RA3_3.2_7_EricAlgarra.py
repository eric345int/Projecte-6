
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer les hores d'un rellotge en concret les hores incials,que ho retorni, establir les hores,i el rang han de ser entre 0 i 23 i el metode per mostrar les hores.

#Especificacions d'entrada:funcio per per a sapiguer les hores d'un rellotge en concret les hores incials,que ho retorni, establir les hores,i el rang han de ser entre 0 i 23 i el metode per mostrar les hores.


class Rellotge:
    def __init__(self, hores_inicials=0):
        self.__hores = hores_inicials

    @property
    def hores(self):
        return self.__hores

    @hores.setter
    def hores(self, valor):
        if 0 <= valor <= 23:
            self.__hores = valor
        else:
            print("Les hores han de ser entre 0 i 23.")

    def mostrar_hores(self):
        return f"{self.__hores:02d}:00"
