# =================================
# EJEMPLO 1: MAYOR O MENOR DE EDAD
# =================================

edad = int(input('¿Cuántos años tienes?: '))

if edad >= 18:
    print('Eres mayor de edad.')
else:
    print('Eres menor de edad.')


# =================================
# EJEMPLO 2: CLASIFICACIÓN CON ELIF
# =================================

nota = float(input('\nIngresa una nota (0 a 100): '))

if nota >= 90:
    print('Excelente')
elif nota >= 70:
    print('Bien')
elif nota >= 50:
    print('Regular')
else:
    print('Reprobado')

# ==================================
# EJEMPLO 3: CON OPERADORES LÓGICOS
# ==================================

edad = int(input('\nCuántos años tienes?: '))
tiene_licencia =  input('¿Tienes licencia de conducir? (si/no): ')

if edad >= 18 and tiene_licencia == 'si':
    print('Puedes conducir.')
elif edad >= 18 and tiene_licencia == 'no':
    print('Eres mayor de edad, pero necesitas licencia.')
else:
    print('No puedes conducir.')
