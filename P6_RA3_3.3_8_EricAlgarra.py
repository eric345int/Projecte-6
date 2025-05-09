

#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer el sou d'un empleat el qual hi pot ser fixe,autonom, i mostrar-ho.

#Especificacions d'entrada:funcio per sapiguer el sou d'un empleat el qual hi pot ser fixe,autonom, i mostrar-ho.

class Empleat:
    def calcular_sou(self):
        pass

class Fixe(Empleat):
    def calcular_sou(self):
        return 2000

class Autonom(Empleat):
    def calcular_sou(self):
        return 1500 - 300  # despeses

def mostrar_sous(llista_empleats):
    for emp in llista_empleats:
        print(f"Sou: {emp.calcular_sou()} €")


