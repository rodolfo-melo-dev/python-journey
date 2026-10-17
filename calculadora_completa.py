# =====================================
# Ejercicio 4: calculadora_completa.py
# =====================================
while True:
    print('\n===CALCULADORA===')
    
    print('Opción 1. SUMAR ')
    print('Opción 2. RESTAR ')
    print('Opción 3. MULTIPLICAR ')
    print('Opción 4. DIVIDIR ')
    print('Opción 5. SALIR ')

    
    opcion= input('Escoge una de las opciones anteriores: ')

    
    
    if opcion == '1':

        num1 = int(input('Ingresa el primer número: '))
        num2 = int(input('Ingresa el segundo número: ')) 
        
        resultado = num1 + num2

        print(f'El resultado de la suma es: {resultado}')

    elif opcion == '2':
        
        num1 = int(input('Ingresa el primer número: '))
        num2 = int(input('Ingresa el segundo número: ')) 
    
        resultado = num1 - num2

        print(f'El resultado de la resta es: {resultado}')

    elif opcion == '3':
        
        num1 = float(input('Ingresa el primer número: '))
        num2 = float(input('Ingresa el segundo número: ')) 
        
        resultado = num1 * num2

        print(f'El resultado de la multiplicación es: {resultado}')

    elif opcion == '4':
        
        num1 = float(input('Ingresa el primer número: '))
        num2 = float(input('Ingresa el segundo número: ')) 
        
        
        
        if num2 == 0:
          
            print('El número no se puede dividir por cero')
                  
        else:
            resultado = num1 / num2
            
            print(f'El resultado de la división es: {resultado}')

    elif opcion == '5':

        print('Hasta luego')

        break

    else:
        print('Opción no válida.')