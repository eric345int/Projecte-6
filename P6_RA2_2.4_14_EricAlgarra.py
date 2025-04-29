parells = []
senars = []
for i in range(10):
    n = int(input(f"Número {i+1}: "))
    if n % 2 == 0:
        parells.append(n)
    else:
        senars.append(n)
print("Parells:", parells)
print("Senars:", senars)
