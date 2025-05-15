
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer els descomptes quant hi descompten, afegir un producte i el total del producte amb el descompte.

#Especificacions d'entrada:funcio per a sapiguer els descomptes quant hi descompten, afegir un producte i el total del producte amb el descompte.

class Descompte20:
    def aplicar(self, total):
        return total * 0.8 if total > 100 else total

class CarretCompra:
    def __init__(self, descompte):
        self.productes = []
        self.descompte = descompte

    def afegir_producte(self, preu):
        self.productes.append(preu)

    def calcular_total(self):
        total = sum(self.productes)
        return self.descompte.aplicar(total)


descompte = Descompte20()
carret = CarretCompra(descompte)
carret.afegir_producte(50)
carret.afegir_producte(60)
print("Total amb descompte:", carret.calcular_total())
