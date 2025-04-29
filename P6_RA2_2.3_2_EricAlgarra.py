try:
    n = int(input("Introdueix un número enter positiu: "))
    if n > 0:
        print("La suma és:", sum(range(1, n + 1)))
    else:
        print("Error: Has d'introduir un número positiu.")
except ValueError:
    print("Error: Has d'introduir un número enter.")
