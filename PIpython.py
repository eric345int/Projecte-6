PI = 3.14                 # Constant

def area(r):             # Funció
    return PI * r * r

radi = float(input("Radi: "))  # Llegeix dades de l’usuari (entrada)
resultat = area(radi)          # Variable
print("Àrea:", resultat)       # Mostra el resultat (sortida)
