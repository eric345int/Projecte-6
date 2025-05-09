

#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a  sapiguer el model,marca i any d'un cotxe,he creat dos cotxes.

#Especificacions d'entrada:aixo hi serveix per a  sapiguer el model,marca i any d'un cotxe,i els cotxes que he creat .


class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_informacio(self):
        print(f"Marca: {self.marca}, Model: {self.model}, Any: {self.any}")


cotxe1 = Cotxe("BMW", "X5", 2022)
cotxe2 = Cotxe("Audi", "Q7", 2021)


cotxe1.mostrar_informacio()
cotxe2.mostrar_informacio()