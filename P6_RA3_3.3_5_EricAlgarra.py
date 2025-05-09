

#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer el tiotl i elautor d'un llibre mostrar-ho ,sapiguer el titol, autor i el nombre de pagines de un llibre de paper i el titol,autor de un llibre en digitali que hi dongui resposta.

#Especificacions d'entrada:funcio per a sapiguer el tiotl i elautor d'un llibre mostrar-ho ,sapiguer el titol, autor i el nombre de pagines de un llibre de paper i el titol,autor de un llibre en digitali que hi dongui resposta.


class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}")

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pagines):
        super().__init__(titol, autor)
        self.n_pagines = n_pagines

    def mostrar_info(self):
        print(f"{self.titol} de {self.autor}, {self.n_pagines} pàgines.")

class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format):
        super().__init__(titol, autor)
        self.format = format

    def mostrar_info(self):
        print(f"{self.titol} de {self.autor}, Format: {self.format}")

