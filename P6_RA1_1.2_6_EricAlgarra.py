lletra = input("Introdueix una lletra: ").lower()

if lletra in "aeiou":
    print("És una vocal.")
elif lletra.isalpha():
    print("És una consonant.")
else:
    print("No has introduït una lletra vàlida.")
