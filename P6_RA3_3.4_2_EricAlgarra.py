
#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer una comanda ,notificar amb un correu electronic i un sms.

#Especificacions d'entrada:funcio per a sapiguer una comanda ,notificar amb un correu electronic i un sms.



class Comanda:
    def __init__(self, notificador):
        self.notificador = notificador

    def confirmar(self):
        self.notificador.enviar("Comanda confirmada")


class NotificadorEmail:
    def enviar(self, missatge):
        print(f"Email: {missatge}")

class NotificadorSMS:
    def enviar(self, missatge):
        print(f"SMS: {missatge}")


c1 = Comanda(NotificadorEmail())
c1.confirmar()

c2 = Comanda(NotificadorSMS())
c2.confirmar()
