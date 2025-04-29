def es_primer(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    n = int(input("Introdueix un número enter positiu: "))
    if n >= 2:
        for i in range(2, n + 1):
            if es_primer(i):
                print(i)
    else:
        print("Error: El número ha de ser 2 o més.")
except ValueError:
    print("Error: Has d'introduir un número enter.")
