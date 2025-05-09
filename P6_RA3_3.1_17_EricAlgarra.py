#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a  sapiguer el nom,especie d'un animal i per a sapiguer el nom de un animal en aquest cas el gos i el soroll que hi fa .

#Especificacions d'entrada:funcio per a sapiguer el nom,especie d'un animal i per a sapiguer el nom de un animal en aquest cas el gos i el soroll que hi fa  .


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


  
