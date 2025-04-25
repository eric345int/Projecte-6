try:
  numero_str = input("Introdueix un número: ")
  numero = float(numero_str)
  if numero > 0:
    print("El número és positiu!")
  elif numero < 0:
    print("El número és negatiu!")
  else:
    print("El número és zero!")
  print("Gràcies!")
except ValueError:
  print("Has introduït un valor no vàlid. Si us plau, introdueix un número.")