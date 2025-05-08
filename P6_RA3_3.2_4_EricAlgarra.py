
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.

class Usuari:
    def __init__(self, nom, contrasenya_inicial):
        self.nom = nom
        self.__contrasenya = contrasenya_inicial

    def canviar_contrasenya(self, nova_contrasenya):
        """Mètode per canviar la contrasenya (mínim 8 caràcters)"""
        if len(nova_contrasenya) >= 8:
            self.__contrasenya = nova_contrasenya
        else:
            print("La contrasenya ha de tenir almenys 8 caràcters.")

    def verificar_contrasenya(self, clau):
        """Mètode per verificar si la contrasenya és correcta"""
        return self.__contrasenya == clau
