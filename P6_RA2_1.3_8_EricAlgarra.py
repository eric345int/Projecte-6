frase = input("Introdueix una frase: ").lower()
vocals = "aeiou"
comptador = 0

for lletra in frase:
    if lletra in vocals:
        comptador += 1

print("Nombre de vocals:", comptador)
