
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer  el nom  i l'especie d'un animal.

#Especificacions d'entrada:funcio per sapiguer el nom i l'especie d'un animal.



class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    def fer_soroll(self):
        print("Fa un soroll.")