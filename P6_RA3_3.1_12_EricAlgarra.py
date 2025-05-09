#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un rectangle i que apareixi per pantalla.

#Especificacions d'entrada:funcio que serveix per a calcular un rectangle i que apareixi per pantalla.


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
