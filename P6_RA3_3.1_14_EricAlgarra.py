#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a  sapiguer quants diners s'han ingresat i quants s'han retirat d'un compte bancari i que hi apareixin per pantalla.

#Especificacions d'entrada:funcio per a sapiguer quants diners s'han ingresat,retirat d'un compte bancari.


class CompteBancari:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def ingressar(self, quantitat):
        self.saldo += quantitat
        print(f"S'han ingressat {quantitat}€. Nou saldo: {self.saldo}€.")

    def retirar(self, quantitat):
        if quantitat <= self.saldo:
            self.saldo -= quantitat
            print(f"S'han retirat {quantitat}€. Nou saldo: {self.saldo}€.")
        else:
            print("Saldo insuficient per a aquesta retirada.")

    def veure_saldo(self):
        print(f"El saldo actual és: {self.saldo}€.")


compte = CompteBancari(500)

compte.ingressar(200)  
compte.retirar(150)    
compte.retirar(700)    
