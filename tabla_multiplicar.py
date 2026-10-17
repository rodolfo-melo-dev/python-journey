# =================================
# Ejercicio : tabla_multiplicar.py
# =================================

print('\nTABLA DE MULTIPLICAR')

i = 0

tabla = int(input('\nIngresa la tabla de multiplicar que quieres ver: '))


for i in range(1, 11):
    
    print(f'{tabla} * {i} = {tabla * i}')

