# Ejercicio para solicitar los datos básicos del usuario

name = input('Hola, ¿Cómo es tu nombre?: ')
age = int(input(f'{name}, ¿Cuántos años tienes?: ' ))
city = input('¿En qué ciudad vives?: ')
age_10 = (age + 10)

print(f'\n{name}, {city} es una bella ciudad, en 10 años tendrás {age_10} años.')

