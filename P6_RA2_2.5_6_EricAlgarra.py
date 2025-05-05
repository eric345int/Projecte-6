#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:13

#Descripció:aixo hi serveix per a calcular nombres i mostrar la resposta.

#Especificacions d'entrada:funcio per calcular nombres i mostrar la resposta.


def multiplica_tot(*nombres):
    resultat = 1
    for n in nombres:
        resultat *= n
    return resultat

print(multiplica_tot(2, 3, 4))
print(multiplica_tot(5, 10))
