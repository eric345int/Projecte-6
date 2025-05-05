#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular i dir si el numero es parell o no

#Especificacions d'entrada:funcio per calcular i dir si un numero es parell o no.

   
def es_parell(numero):
    return numero % 2 == 0

for numero in [1, 2, 3, 4, 5, 6]:
    print(f"El número {numero} és parell: {es_parell(numero)}")
