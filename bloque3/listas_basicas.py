# ===============oo=============
# Ejemplos listas_basicas.py
# ===============oo=============

frutas = ['manzana', 'pera', 'uva']
print(frutas)
print(type(frutas))

''' ==============00===============
  Así se imprimen las listas elementos por separado. Subindices entre los corchetes.
  subindices desde 0 que es el primer elemento. 
================00=============='''

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[-1])
print(frutas[-2])

'''=============000=========
   Slicing son una forma de construir una nueva lista con parte
   de los elementos de una listas
   ============000=========='''

print(frutas[1:3])
print(frutas[2:3])
print(frutas[2:])
print(frutas[:2])

'''=========000========
   len se utiliza para saber cuantos elementos tiene una lista
   =========000========'''

print(len(frutas))

'''=========000========
    mutabilidad: se pueden cambiar elementos de una lista,
    usando la lista y el elemento que e quiere cambiar entre corchetes.
    por ejemplo lista[0]
    ========000========'''

frutas[1] = 'patilla'

print(frutas)
'''EJERCICIOS'''

'''==EJERCICIO 1=='''

colores = ['amarillo', 'azul', 'rojo', 'blanco']

print(colores)

print(len(colores))

'''==EJERCICIO 2=='''

print(colores[0])
print(colores[1])
print(colores[-1])

'''==EJERCICIO 3=='''

print(colores[0:2]) # ESTOS DOS CASOS DAN EL MISMO RESULTADO
print(colores[:2])
print(colores[2:]) # aquí se imprimen los dos últimos

'''==EJERCICIO 4=='''

colores[3] = 'verde'

print(colores)

'''==EJERCICIO 5=='''

miscelanea = ['Alejandra', 33, True]

print(miscelanea)

print(miscelanea[0])
print(miscelanea[1])
print(miscelanea[2])