#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.


class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

    def aplicar_descompte(self, percentatge):
        descompte = (percentatge / 100) * self.preu
        self.preu -= descompte
        print(f"El nou preu després del descompte és: {self.preu}€")


def aplicar_descompte_a_products(productes):
    for producte in productes:
        producte.aplicar_descompte(10)


producte1 = Producte("Portàtil", 1000)
producte2 = Producte("Smartphone", 600)
producte3 = Producte("Tablet", 300)

productes = [producte1, producte2, producte3]


aplicar_descompte_a_products(productes)
