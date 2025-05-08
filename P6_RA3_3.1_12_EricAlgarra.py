#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.



class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre):
        return ((self.x - altre.x) ** 2 + (self.y - altre.y) ** 2)
class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada

    def area(self):
        return self.amplada * self.alçada


rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(7, 4)
rectangle3 = Rectangle(6, 8)


print(f"Area Rectangle 1: {rectangle1.area()}")
print(f"Area Rectangle 2: {rectangle2.area()}")
print(f"Area Rectangle 3: {rectangle3.area()}")
