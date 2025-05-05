import random

def llençar_dau():
    return random.randint(1, 6)

def mitjana_daus(n):
    resultats = [llençar_dau() for _ in range(n)]
    return sum(resultats) / n

print("Dau:", llençar_dau())
print("Mitjana de 10 tirades:", mitjana_daus(10))


