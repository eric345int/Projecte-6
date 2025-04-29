try:
    n = int(input("Introdueix un número enter: "))
    for i in range(n + 1):
        print(i)
except ValueError:
    print("Error: Has d'introduir un número enter.")
