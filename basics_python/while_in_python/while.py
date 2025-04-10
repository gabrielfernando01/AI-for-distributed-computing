# =====================================================================
# Sentence while in Python
while condition:
    block code

n = 0
print('First 10 multiples of 11')
while n <= 10:
    print(f'{n * 11}')
    n += 1
print('End')

# ======================================================================
# Suppose we want to know if an element (7) is contained in a list.
values = [6, 3, 2, 7, 1, 23]

found = False
index = 0
lenght = len(values)
while not found and index < lenght:
    value = values[index]
    if value == 7:
        found = True
    else:
        index += 1
if found:
    print(f'El número 7 ha sido encontrado en el indice {index}')
else:
    print('El número 7 no se encuentra en la lista de valores')

# =========================================================================
# Añadiendo la sentencia break al ejemplo anterior.
values = [6, 3, 2, 7, 1, 23]

found = False
index = 0
lenght = len(values)
while index < lenght:
    value = values[index]
    if value == 7:
        found = True
        break
    else:
        index += 1
if found:
    print(f'El elemento 7 ha sido encontrado en el indice {index}')
else:
    print(f'El elemento 7 no se encuentra en la lisa de valores')

# ===========================================================================
# Another modification is:
values = [6, 3, 2, 7, 1, 23]

index = 0
lenght = len(values)
while index < lenght:
    value = values[index]
    if value == 7:
        print(f'EL elemento 7 ha sido encontrado en el indice {index}')
        break
    else:
        index += 1
else:
    print('El elemento 2 no se encuentra en la lista de valores')













