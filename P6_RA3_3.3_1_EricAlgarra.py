

#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per identifica com hi parla un animal, un gos hi fa bup bup i un gat hi fa miau.

#Especificacions d'entrada:funcio  identifica com hi parla un animal, un gos hi fa bup bup i un gat hi fa miau.

class Animal:
    def parlar(self):
        print("L'animal fa un soroll.")

class Gos(Animal):
    def parlar(self):
        print("Bup bup!")

class Gat(Animal):
    def parlar(self):
        print("Miau!")


