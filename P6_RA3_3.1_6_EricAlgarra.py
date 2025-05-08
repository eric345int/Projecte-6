

#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer el saldo  calcular la quantitat de diners i mostra-ho.

#Especificacions d'entrada:funcio per sapiguer el saldo, calcular la quantitat de diners i mostra-ho.


class CompteBancari:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def ingressar(self, quantitat):
        self.saldo += quantitat

    def retirar(self, quantitat):
        if quantitat <= self.saldo:
            self.saldo -= quantitat
        else:
            print("Saldo insuficient.")

    def veure_saldo(self):
        print("Saldo actual:", self.saldo)