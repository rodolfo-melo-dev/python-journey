# Explicación de diccionarios ==

persona = {                         # Los diccionarios se crean con {} donde se colocan los valores de a pares uno frente al otro con ':' y entre comillas '' 
    'nombre' : 'Alejandra',
    'edad' : 35,
    'pais' : 'Colombia'

}
print(persona['nombre'])            # Para acceder a los datos la clave debe in entre corchetes[] y entre comillas ''
print(persona ['edad'])
print(persona['pais'])

# Para modificar un valor 

persona['edad'] = 36

print(persona['edad'])  # Para ver reflejado el cambio se debe imprimir de nuevo la clave a la que se le hizo el cambio
print(persona)         # Para ver el diccionario completo se debe simplemente imprimir persona

# Para agregar una nueva clave 

persona['profesion'] = 'madre de mis hijos'
print(persona)

# Para evitar errores se utiliza despues del nombre del diccionario .get y la clave 

print(persona.get('nombre'))
print(persona.get('correo'))
print(persona.get('correo', 'No regiistrado'))

# Usando for - in se el programa recorrera todas las claves y sus pares

for clave in persona:
    print(clave)

# for con clave, valor in nombre del diccionario y .items hace un listado de cada par por separado 

for clave, valor in persona.items():
    print(f'{clave}, {valor}')

# == Ejercicio 1 ==

libro = {

'titulo' : 'La Biblia',
'autor' : 'Dios',
'año' : '10.000 AC'

}

print(libro['titulo'])
print(libro['autor'])
print(libro['año'])

for clave, valor in libro.items():
    print(f'{clave},{valor}')

# == Ejercicio 2 ==

libro['año'] = '9000 AC'

libro['genero'] = 'Historia'

for clave, valor in libro.items():
    print(f'{clave},{valor}')

    # == Ejercicio 3 ==

dato = input('¿Que dato del libro quieres?')

print(libro.get(dato))


# == Ejercicio 4 ==

for clave, valor in libro.items():
    print(f'{clave}, {valor}')

    