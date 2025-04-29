frase = input("Escriu paraules separades per espai: ")
paraules = frase.split()
vocal_inici = [p for p in paraules if p[0].lower() in "aeiou"]
print(vocal_inici)
