
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.


class Estudiant:
    def __init__(self, nom, nota_inicial=0):
        self.nom = nom
        self._nota = nota_inicial

    def llegir_nota(self):
        """Llegir la nota de l'estudiant"""
        return self._nota

    def modificar_nota(self, nova_nota):
        """Modificar la nota només si és entre 0 i 10"""
        if 0 <= nova_nota <= 10:
            self._nota = nova_nota
        else:
            print("Nota no vàlida. La nota ha de ser entre 0 i 10.")
