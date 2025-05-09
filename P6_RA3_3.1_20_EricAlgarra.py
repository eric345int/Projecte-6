#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer el nom i la edat d'una persona ,he afegit persones i tambe es mostraran les persones que hi tinguin mes que 30 anys.

#Especificacions d'entrada:funcio per per a sapiguer el nom i la edat d'una persona..


class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat


def mostrar_persones_major_30(persones):
    for persona in persones:
        if persona.edat > 30:
            print(f"{persona.nom} té {persona.edat} anys i té més de 30 anys.")

persona1 = Persona("Joan", 25)
persona2 = Persona("Anna", 35)
persona3 = Persona("Jordi", 40)

persones = [persona1, persona2, persona3]


mostrar_persones_major_30(persones)
