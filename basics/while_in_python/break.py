# Usaremos el comando break para romper y salir del 
# bucle, una vez que se haya culplido la condición 
valores = [5, 4, 7, 0, 9, 2, 1]

encontrado = False
indice = 0
longitud = len(valores)

while indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
        break
    else:
        indice += 1
if encontrado:
    print(f'El elemento 2 ha sido encontrado en el indice {indice}')
else:
    print('El elemento 2 no se encuentra en la lista valores')
