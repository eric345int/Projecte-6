#Administració de Sistemes Informàtics en Xarxa
# Autor:Eric
# Data:5/5/2025

# Versió:12

#Descripció:aixo hi serveix per a sapiguer la factura, i imprimir-la en pdf.

#Especificacions d'entrada:funcio per a sapiguer  la factura, i imprimir-la en pdf.

class Factura:
    def __init__(self, impressora):
        self.impressora = impressora

    def imprimir(self):
        self.impressora.imprimir("Factura impresa")


class Impressora:
    def imprimir(self, text):
        print(text)


class ImpressoraPDF:
    def imprimir(self, text):
        print(f"Generant PDF: {text}")


factura = Factura(Impressora())
factura.imprimir()

factura_pdf = Factura(ImpressoraPDF())
factura_pdf.imprimir()
