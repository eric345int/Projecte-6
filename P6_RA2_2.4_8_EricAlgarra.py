def elimina_espais(cadena):
    return cadena.replace(" ", "")

text = input("Introdueix una cadena: ")
print(elimina_espais(text))
