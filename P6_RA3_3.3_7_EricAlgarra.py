


#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a dibuixar una figura la cual hi pot ser un cercle,un quadrat,un triangle.

#Especificacions d'entrada:funcio per a dibuixar una figura la cual hi pot ser un cercle,un quadrat,un triangle.

class Figura:
    def dibuixar(self):
        pass

class Cercle(Figura):
    def dibuixar(self):
        print("Dibuixant un cercle")

class Quadrat(Figura):
    def dibuixar(self):
        print("Dibuixant un quadrat")

class Triangle(Figura):
    def dibuixar(self):
        print("Dibuixant un triangle")


