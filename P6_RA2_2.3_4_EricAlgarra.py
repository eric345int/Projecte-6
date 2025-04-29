try:
    n = int(input("Introdueix un número enter positiu: "))
    if n >= 0:
        for i in range(0, n + 1, 2):
            print(i)
    else:
        print("Error: El número ha de ser positiu.")
except ValueError:
    print("Error: Has d'introduir un número enter.")
