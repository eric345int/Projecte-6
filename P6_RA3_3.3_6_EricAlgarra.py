

#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per  a sapiguer el soroll d'un animal ,el d'un gat i el d'una vaca i mostra-ho.

#Especificacions d'entrada:funcio per  a sapiguer el soroll d'un animal ,el d'un gat i el d'una vaca i mostra-ho.

class Animal:
    def fer_soroll(self):
        pass

class Gat(Animal):
    def fer_soroll(self):
        return "Miau"

class Vaca(Animal):
    def fer_soroll(self):
        return "Muuu"

def reproduir_soroll(animal):
    print(animal.fer_soroll())


