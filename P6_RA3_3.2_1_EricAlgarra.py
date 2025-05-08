
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a calcular un punt.

#Especificacions d'entrada:funcio per calcular  un punt.

class CompteBancari:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    def ingressar_diners(self, quantitat):
        """Ingressar diners al compte"""
        if quantitat > 0:
            self.__saldo += quantitat
        else:
            print("Quantitat incorrecta per ingressar.")

    def retirar_diners(self, quantitat):
        """Retirar diners del compte"""
        if quantitat > 0 and quantitat <= self.__saldo:
            self.__saldo -= quantitat
        else:
            print("Quantitat incorrecta o saldo insuficient.")

    def consultar_saldo(self):
        """Consultar el saldo del compte"""
        return self.__saldo
