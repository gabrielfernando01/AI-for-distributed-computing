valores = [1, 4, 6, 2, 8, 2]

indice = 0
longitud = len(valores)

while indice < longitud:
    valor = valores[indice]
    if valor == 2:
        print(f'El elemento 2 ha sido encontrado en el indice {indice}')
        break
    else:
        indice += 1
else:
    print('El elemento 2 no se encuentra en la lista de valores')
