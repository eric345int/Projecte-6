
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a crear un compte bancari amb un saldo inicial ingressar diners al compte,dir si la quantitat es incorrecta per a ingresar i dir si el saldo es insuficient i consultar el saldo.

#Especificacions d'entrada:funcio per  a crear un compte bancari amb un saldo inicial ingressar diners al compte,dir si la quantitat es incorrecta per a ingresar i dir si el saldo es insuficient i consultar el saldo.

class CompteBancari:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    def ingressar_diners(self, quantitat):
        if quantitat > 0:
            self.__saldo += quantitat
        else:
            print("Quantitat incorrecta per ingressar.")

    def retirar_diners(self, quantitat):
        if quantitat > 0 and quantitat <= self.__saldo:
            self.__saldo -= quantitat
        else:
            print("Quantitat incorrecta o saldo insuficient.")

    def consultar_saldo(self):
        return self.__saldo
