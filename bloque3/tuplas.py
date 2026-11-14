# == EJERCICIOS DE TUPLAS ==

# == Ejercicio 1 ==

dimensiones = (1920, 1080)

print(dimensiones)
print(dimensiones[0])
print(dimensiones[-1])
print(len(dimensiones))

# == Ejercicio 2 ==

# dimensiones[0] = 1280

# == Ejercicio 3 ==

usuario = ('Alejandra', 'Yate', 'alejayl@gmail.com')

nombre, apellido, correo = usuario

print(nombre)
print(apellido)
print(correo)

# == Ejercicio 4 ==

meses = ('enero', 'febrero', 'marzo', 'abril')

for mes in meses:
    print(f'Este mes es {mes}')
