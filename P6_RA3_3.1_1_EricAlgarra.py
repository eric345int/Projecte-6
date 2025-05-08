#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:6/5/2025

# Versió:15

#Descripció:aixo hi serveix per sapiguer el model,marca,any i mostrar la informacio resultant.

#Especificacions d'entrada:funcio per sapiguer model,marca i any d'un coche i mostrar la resposta.

class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_info(self):
        print(f"{self.marca} {self.model}, {self.any}")