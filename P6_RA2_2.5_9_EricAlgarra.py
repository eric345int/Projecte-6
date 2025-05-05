def estat_persona(edat):
    if edat < 18:
        return "Menor d'edat", "Encara no és adult"
    elif edat < 65:
        return "Adult", "Persona en edat laboral"
    else:
        return "Jubilat", "Ha arribat a l'edat de jubilació"

for edat in [12, 25, 70]:
    estat, desc = estat_persona(edat)
    print(f"Edat {edat}: {estat} - {desc}")
