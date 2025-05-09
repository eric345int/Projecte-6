
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer el valor inicial d'un sensor,obtenir el valor ,establir el valor nomes entre 0 i 100.

#Especificacions d'entrada:funcio per a sapiguer el valor inicial d'un sensor,obtenir el valor ,establir el valor nomes entre 0 i 100.




class Sensor:
    def __init__(self, valor_inicial=0):
        self.__valor = valor_inicial

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if 0 <= valor <= 100:
            self.__valor = valor
        else:
            print("El valor ha de ser entre 0 i 100.")
