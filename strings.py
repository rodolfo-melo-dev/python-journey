name = 'Rodolfo'

print(f'Hola {name}, ¿como estás?')

# ==========***===========
#-- EJERCICIOS DE STRING--
# ==========***===========

# 1. ** TIPOS DE CONCADENACIÓN**

name = 'Rodolfo'
last_name = 'Melo Parra'

print(f'Nombre completo: {name} {last_name}')
print(f'En mayúsculas: {name.upper()} {last_name.upper()}')
print(f'En minúsculas: {name.lower()} {last_name.lower()}')

# 2. **CONTAR CARÁCTERES**

frase = 'Aprender python es un viaje pero no un destino'
print(frase)
print(f'La frase tiene: {len(frase)} carácteres')

# 3. **ACCEDER A CARÁCTERES**

print(F'El primer carácter de la frase es: {frase[0]}')
print(f'El último carácter de la frase es: {frase[-1]}')
print(f'El tercer carácter de la frase es: {frase[2]}')

# 4. **SLICING**

print(f'Los primeros 5 caracteres de la frase son: {frase[:5]}')
print(f'Los últimos 5 caracteres de la frase son: {frase[-5:]}')
print(f'La frase invertida se veria así: {frase[::-1]}')

# 5. **REPLACE**

texto = 'manzana,pera,uva'
print(f'Con guiones quedaría así: {texto.replace (',' , '-')}')
print(f'Lista: {texto.split(',')}')

# 6. **STRIP Y TITLE**

texto_sucio = 'juan pérez'
print(f'Texto limpio y con formato quedaría así: {texto_sucio.strip().title()}')

