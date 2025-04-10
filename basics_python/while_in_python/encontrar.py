# ============================================================
# Usando el bucle while, verificar si un número se encuentra
# contenido en una lista
valores = [5, 1, 9, 2, 7, 4]

encontrado = False
indice = 0
longitud = len(valores)
while not encontrado and indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
    else:
        indice += 1
if encontrado:
    print(f'El número 2 ha sido encontrado en el índice {indice}')
else:
    print('El número 2 no se encuentra en la lista de valores')
