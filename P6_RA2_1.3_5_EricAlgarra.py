num = int(input("Introdueix un número positiu: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} NO és un nombre primer.")
            break
    else:
        print(f"{num} és un nombre primer.")
else:
    print("El número ha de ser més gran que 1.")
