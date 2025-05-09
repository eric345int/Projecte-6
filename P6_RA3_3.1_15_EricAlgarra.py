#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer quin producte es es vol el seu nom i el preu i si shan d'aplicar descomptes i he creat diversos productes.

#Especificacions d'entrada:funcio per a  sapiguer quin producte es es vol el seu nom,el preu  si shan d'aplicar descomptes i he creat diversos productes.


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
