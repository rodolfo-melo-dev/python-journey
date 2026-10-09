# ==============================
# Ejercicio 3: mayor_de_tres.py
# ==========0===================

num1 = float(input('Ingresa el primer número: '))
num2 = float(input('Ingresa el segundo número: '))
num3 = float(input('Ingresa el tercer número: '))

if num1 >= num2 and num1 >= num3:
    print(f'El mayor es: {num1:.0f}.')
elif num2 >= num1 and num2 >= num3:
    print(f'El mayor es: {num2:.0f}.')
else:
    print(f'El mayor es: {num3:.0f}.')

