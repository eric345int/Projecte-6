

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

class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_informacio(self):
        print(f"Marca: {self.marca}, Model: {self.model}, Any: {self.any}")


cotxe1 = Cotxe("BMW", "X5", 2022)
cotxe2 = Cotxe("Audi", "Q7", 2021)


cotxe1.mostrar_informacio()
cotxe2.mostrar_informacio()