#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.

class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Any: {self.any}")


class Biblioteca:
    def __init__(self):
        self.llibres = []

    def afegir_llibre(self, llibre):
        self.llibres.append(llibre)

    def mostrar_llibres(self):
        for llibre in self.llibres:
            llibre.mostrar_info()


llibre1 = Llibre("1984", "George Orwell", 1949)
llibre2 = Llibre("El Petit Príncep", "Antoine de Saint-Exupéry", 1943)

biblioteca = Biblioteca()
biblioteca.afegir_llibre(llibre1)
biblioteca.afegir_llibre(llibre2)



