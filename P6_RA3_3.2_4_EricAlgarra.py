
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a crear un usuari el qual ha de contindre un nom,una contrsenya inicial en la que despres la canviarem per a una de nova i definitiva,els requisits de la contrasenys i per verificar si la contrasenya es correcta.

#Especificacions d'entrada:funcio per crear un usuari el qual ha de contindre un nom,una contrsenya inicial en la que despres la canviarem per a una de nova i definitiva,els requisits de la contrasenys i per verificar si la contrasenya es correcta.

class Usuari:
    def __init__(self, nom, contrasenya_inicial):
        self.nom = nom
        self.__contrasenya = contrasenya_inicial
    def canviar_contrasenya(self, nova_contrasenya):
        if len(nova_contrasenya) >= 8:
            self.__contrasenya = nova_contrasenya
        else:
            print("La contrasenya ha de tenir almenys 8 caràcters.")

    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau
