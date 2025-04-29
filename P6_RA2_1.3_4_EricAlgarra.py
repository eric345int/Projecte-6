import random

secret = random.randint(1, 100)
endevina = 0

while endevina != secret:
    endevina = int(input("Endevina el número (1-100): "))
    if endevina < secret:
        print("Massa baix!")
    elif endevina > secret:
        print("Massa alt!")
print("Correcte! Has endevinat el número!")
