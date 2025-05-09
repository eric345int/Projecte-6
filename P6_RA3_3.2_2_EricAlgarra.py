
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer el nom,  la nota inicial d'un alumne,llegir la nota ,si la nota es menos que 10 posar nota nova i ha de ser entre 0 i 10.

#Especificacions d'entrada:funcio per a sapiguer el nom,  la nota inicial d'un alumne,llegir la nota ,si la nota es menos que 10 posar nota nova i ha de ser entre 0 i 10.


class Estudiant:
    def __init__(self, nom, nota_inicial=0):
        self.nom = nom
        self._nota = nota_inicial

    def llegir_nota(self):
        return self._nota

    def modificar_nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self._nota = nova_nota
        else:
            print("Nota no vàlida. La nota ha de ser entre 0 i 10.")
