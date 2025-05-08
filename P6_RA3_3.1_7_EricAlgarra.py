
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular el radi d'un cercle..

#Especificacions d'entrada:funcio per calcular el radi d'un cercle.


class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return   self.radi ** 2

    def perimetre(self):
        return 2 *   self.radi