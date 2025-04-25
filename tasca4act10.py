num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))

print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicació:", num1 * num2)
if num2 != 0:
    print("Divisió:", num1 / num2)
else:
    print("No es pot dividir per zero.")
