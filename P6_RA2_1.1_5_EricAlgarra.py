from datetime import date

any_naixement = int(input("Introdueix l'any de naixement: "))
mes_naixement = int(input("Introdueix el mes de naixement (1-12): "))
dia_naixement = int(input("Introdueix el dia de naixement: "))

avui = date.today()
data_naixement = date(any_naixement, mes_naixement, dia_naixement)

edat = avui.year - data_naixement.year
if (avui.month, avui.day) < (data_naixement.month, data_naixement.day):
    edat -= 1

print(f"Tens {edat} anys.")

if edat >= 18:
    print("Ets major d'edat.")
else:
    print("Ets menor d'edat.")

