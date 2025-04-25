minuts_totals = int(input("Introdueix el nombre de minuts: "))
hores = minuts_totals // 60
minuts = minuts_totals % 60
print(f"{minuts_totals} minuts són {hores} hores i {minuts} minuts")
