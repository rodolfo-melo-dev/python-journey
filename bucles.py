# =========================
# Ejemplo 1: for con range
# =========================

print('---Ejemplo 1: For con range---')
for i in range(5):
    print(i)

# =================
# Ejemplo 2: while 
# =================

print('\n---Ejemplo 2: while---')

contador = 0
while contador < 5:
    print(contador)
    contador += 1


# =================
# Ejemplo 3: break
# =================

print('\n---Ejemplo 3: break---')

for i in range(10):
    if i == 5:
        break
    print(i)


# ====================
# Ejemplo 4: continue
# ====================

print('---\nEjemplo 4: continue---')

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# ================================================
# Ejemplo 5: Ejemplo propio, Solo pares con while
# ================================================
print('---\nEjemplo 5:  Ejemplo propio, continue pero solo los pares---')

for i in range(10):
    if i % 2 != 0:
        continue
    print(i)

