
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer el titol,autor,any de un llibre .

#Especificacions d'entrada:funcio a sapiguer el titol,autor,any de un llibre.

class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        print(f"{self.titol} de {self.autor} ({self.any})")