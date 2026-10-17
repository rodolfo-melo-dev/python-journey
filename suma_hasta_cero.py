# ================================
# Ejercicio 2: suma_hasta_cero.py
# ================================

suma = 0 

while True != 0:
    num = int(input('Ingresa un número (0 para salir): '))

    if num == 0:
        break
    
    suma += num 
print(f'La suma total es: {suma}')



