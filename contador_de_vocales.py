# ====================================
# Ejercicio 3: contador_de_vocales.py
# ====================================
frase = input('Ingresa una frase: ')

contador = 0

for letra in frase.lower():
    if letra in 'aeiou':
        contador += 1

print(f'El número de vocales en la frase es: {contador} ')

