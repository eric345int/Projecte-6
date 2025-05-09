

#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer de una persona un nom la edat ,com hi saluda una person , un trballador cal sapiguer el nom,l'edat i quina feina hi te i a on hi treballa .

#Especificacions d'entrada:funcio per  a sapiguer de una persona un nom la edat ,com hi saluda una person , un trballador cal sapiguer el nom,l'edat i quina feina hi te i a on hi treballa ..

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def saludar(self):
        print(f"Hola, sóc {self.nom}")

class Treballador(Persona):
    def __init__(self, nom, edat, feina):
        super().__init__(nom, edat)
        self.feina = feina

    def mostrar_feina(self):
        print(f"Treballo com a {self.feina}")


