# 10. Assegurar el tancament del fitxer amb try-finally
fitxer = None
try:
    fitxer = open("missatge.txt", "r", encoding="utf-8")
    print("Llegeixo contingut:")
    print(fitxer.read())
    # Simula un error (descomenta per provar)
    # raise Exception("Error simulat durant la lectura.")
except Exception as e:
    print("S'ha produït un error:", e)
finally:
    if fitxer:
        fitxer.close()
        print("Fitxer tancat correctament (fins i tot amb error).")
