text = input("Escriu una frase: ")
vowels = "aeiouAEIOU"
comptador = sum(1 for c in text if c in vowels)
print("Hi ha", comptador, "vocals.")
