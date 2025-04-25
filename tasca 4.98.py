# a. Una constant
SALUTACIO = "Hola, "

# b. Una funció
def saludar(nom):
  """Aquesta funció saluda a la persona amb el nom proporcionat."""
  missatge = SALUTACIO + nom + "!"
  return missatge

# c. Una entrada de l’usuari
nom_usuari = input("Si us plau, introdueix el teu nom: ")

# d. Una sortida per pantalla
salutacio_final = saludar(nom_usuari)
print(salutacio_final)