try:
    n = int(input("Introdueix un número enter: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
except ValueError:
    print("Error: Has d'introduir un número enter.")
