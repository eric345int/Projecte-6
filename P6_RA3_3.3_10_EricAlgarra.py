

#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer de diferents vehicles per a on hi van per exemple un cotxe per la carretera o una bicicleta pel carril bici.

#Especificacions d'entrada:funcio per a sapiguer de diferents vehicles per a on hi van per exemple un cotxe per la carretera o una bicicleta pel carril bici.

class Vehicle:
    def moure(self):
        pass

class Cotxe(Vehicle):
    def moure(self):
        print("El cotxe condueix per la carretera.")

class Bicicleta(Vehicle):
    def moure(self):
        print("La bicicleta es desplaça pel carril bici.")

class Barca(Vehicle):
    def moure(self):
        print("La barca navega pel riu.")

def simular_moviment(vehicles):
    for v in vehicles:
        v.moure()


