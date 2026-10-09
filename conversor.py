# CONVERSOR DE DÓLARES

tasa = float(input("Tasa de cambio (COP por USD): "))
pesos = float(input("Cantidad de pesos: "))

dolares = pesos / tasa

print(f"\nCon {pesos:.2f} COP obtienes {dolares:.2f} USD.")