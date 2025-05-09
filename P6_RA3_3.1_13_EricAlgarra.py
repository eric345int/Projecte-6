#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer quants estudiants hi han i dir si as aprovat o no..

#Especificacions d'entrada:funcio per a sapiguer quants estudiants hi han hi si han aprovat o no.


class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    def ha_aprovat(self):
        return self.nota >= 5


estudiant1 = Estudiant("Marc", 6)
estudiant2 = Estudiant("Maria", 4)
estudiant3 = Estudiant("Jordi", 8)

estudiants = [estudiant1, estudiant2, estudiant3]


for estudiant in estudiants:
    if estudiant.ha_aprovat():
        print(f"{estudiant.nom} ha aprovat!")
