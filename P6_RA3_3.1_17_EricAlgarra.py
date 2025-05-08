#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.


class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    def fer_soroll(self):
        print(f"{self.nom} fa un soroll.")


class Gos(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Canis lupus familiaris")

    def fer_soroll(self):
        print(f"{self.nom} fa: Bup bup!")


gos1 = Gos("Rex")
gos1.fer_soroll()  
