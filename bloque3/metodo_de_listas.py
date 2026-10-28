''' ==MÉTODOS DE LISTAS=='''

'''Los métodos de listas no hacen una lista nueva, modifican una ya creaada. Los métodos de 
    lista se utilizan así: lista.metodo()'''

frutas = ['manzana','kiwi']

print(frutas)

frutas.append('uva') # .append añade un nuevo elemento a la lista. 

print(frutas)

frutas.insert(2, 'melón') 
'''.insert inserta, añade un elemento en una posición determinada. Se coloca el número
de la posición recordar que la posición siendo la primera 0 y separado por coma el elemento a insertar. '''

print(frutas)

frutas.remove('manzana')
'''.remove remueve un elemento de una lista, el elemento a remover esta entre comillas y entre parentesis.'''

print(frutas)

ultima = frutas.pop()

''' .pop muestra el último elemento y devuelve la lista sin el último elemento.'''

print(ultima)

print(frutas)

print(frutas.index('melón'))
'''.index muestra el lugar o pocisión donde se encuentra un elemento en una lista'''

print(frutas.count('kiwi'))
'''.count muestra el número de veces en que aparece un elemento de una lista'''

numeros = [1, 9, 0, 5, 3, 12, 6]

print(numeros)

numeros.sort()
'''.sort ordena una lista de forma alfabetica o númerica'''

print(numeros)

names = ['Alejandra', 'Daniela', 'Luna', 'Juliana']

sorted(names)

names.sort()

print(names)

numeros.reverse()

print(numeros)

names.reverse()
'''.reverse devulve una lista ordenada en inversa, es decir de mayor a menor, ya sea númerica o alfabética'''

print(names)

# ==============00===============
# Ejercicios de métodos de listas
# ===============================

# ==Ejercicio 1==

novias = ['Alejandra', 'Daniela']

print(novias)

novias.append('Juliana')

print(novias)

novias.insert(0, 'Luna')

print(novias)

# ==Ejercicio 2==

novias.remove('Alejandra')

print(novias)

ultimo = novias.pop()

print(ultimo)

print(novias)

# ==Ejercicio 3==

precios = [45, 12, 89, 33, 7]

print(precios)

precios.sort()

print(precios)

precios.reverse()

print(precios)

# ==Ejercicio 4==

notas = [5, 3, 5, 4, 5, 2]

print(notas.index(4))

print(notas.count(5))
