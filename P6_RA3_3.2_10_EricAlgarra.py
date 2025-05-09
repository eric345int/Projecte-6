
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a crear un compte de usuari el qual hi tingui un email inicial,sapiguer si ets el propietari i el  valor del email i mostra-ho.

#Especificacions d'entrada:funcio per a crear un compte de usuari el qual hi tingui un email inicial,sapiguer si ets el propietari i el  valor del email i mostra-ho.


class CompteUsuari:
    def __init__(self, email_inicial):
        self.__email = email_inicial

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if "@" in valor and "." in valor:
            self.__email = valor
        else:
            print("L'email ha de contenir '@' i '.'")

