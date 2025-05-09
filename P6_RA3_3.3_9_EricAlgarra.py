

#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a enviar missatges el qual hi poden ser email,sms,Whatsapp.

#Especificacions d'entrada:funcio per a enviar missatges el qual hi poden ser email,sms,Whatsapp .

class Missatger:
    def enviar(self, missatge):
        pass

class Email(Missatger):
    def enviar(self, missatge):
        print(f"Enviant Email: {missatge}")

class SMS(Missatger):
    def enviar(self, missatge):
        print(f"Enviant SMS: {missatge}")

class WhatsApp(Missatger):
    def enviar(self, missatge):
        print(f"Enviant WhatsApp: {missatge}")

def enviar_missatges(missatgers, missatge):
    for m in missatgers:
        m.enviar(missatge)


