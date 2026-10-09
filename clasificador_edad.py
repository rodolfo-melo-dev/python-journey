# =============================
# Ejercicio 2: clasificador.py
# =============================

edad = int(input('Por favor ingresa tu edad: '))

if edad < 12:
    print('Niño.')
elif edad < 18:
    print('Adolescente.')
elif edad < 65:
    print('Adulto.')
else:
    print('Adulto mayor.')
