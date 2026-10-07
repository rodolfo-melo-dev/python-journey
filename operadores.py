# OPERADORES ÁRITMETICOS 
#============================= 
print("--ÁRITMETICOS--")

print(10 + 3)    # Suma
print(10 - 3)    # Resta
print(10 * 3)    # Multiplicación
print(10 / 3)    # División
print(10 // 3)   # División Entera
print(10 % 3)    # Módulo (Residuo)
print(10 ** 3)   # Potencia

# =========================
# "OPERACIONES COMPARATIVAS"
# ==========================

print("--COMPARACIÓN--")

print(5 > 3)    #  True
print(5 < 3)    #  False
print(5 == 5)   #  True
print(5 != 3)   #  True
print(5 >= 5)   #  True
print(5 <= 4)   #  False

# =======================
# "OPERADORES LÓGICOS"
# =======================

print("--LÓGICOS--")

print(True and False)   #  False
print(True or False)    #  True
print(not True)         #  False

# =================
# --EJERCICIOS--
# =================
print("--EJERCICOS--")

# 1. Segundos en 3 días 

segundos_en_tres_dias = 3 * 24 * 60 * 60
print(f"Los segundos que tiene 3 días son:  {segundos_en_tres_dias}")

# 2. Cuántos dulces de 7 pesos puedo comprar con 1000 pesos

dulces = 1000 // 7
residuo = 1000 % 7
print(f"Con mil pesos puedo comprar {dulces} y me sobran {residuo} pesos")

# 3. Eleva 2 a la 10

print(f"2 elevado a la 10 es: {2**10}")

# 4. Verifica si 15 es mayor que 10

print(f"¿15 es mayor que 10? {15 > 10}")


# 5. Verificar si 7 es par 

print(f"¿El número 7 es par?  {7 % 2 == 0}")