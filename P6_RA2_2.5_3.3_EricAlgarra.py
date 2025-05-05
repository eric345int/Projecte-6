from datetime import datetime, date

ara = datetime.now()
print("Data actual:", ara.strftime("%d/%m/%Y %H:%M"))

nadal = date(2025, 12, 25)
avui = date.today()
dies_falten = (nadal - avui).days
print(f"Falten {dies_falten} dies per Nadal.")
