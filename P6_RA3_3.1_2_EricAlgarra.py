#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:6/5/2025

# Versió:16

#Descripció:aixo hi serveix per a sapiger la amplada i la alçada d'un rectangle.

#Especificacions d'entrada:aquesta funcio hi serveix per a sapiguer la amplada i la alçada d'un triangle.


class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada

    def area(self):
        return self.amplada * self.alçada

    def perimetre(self):
        return 2 * (self.amplada + self.alçada)