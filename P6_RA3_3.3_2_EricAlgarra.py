
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer la marca d'un vehicle com arrancar i quin soroll hi fa..

#Especificacions d'entrada:funcio per a sapiguer la marca d'un vehicle com arrancar i quin soroll hi fa..

class Vehicle:
    def __init__(self, marca):
        self.marca = marca

    def arrencar(self):
        print(f"{self.marca} arrencant...")

class Cotxe(Vehicle):
    def tocar_claxon(self):
        print("Pip pip!")


