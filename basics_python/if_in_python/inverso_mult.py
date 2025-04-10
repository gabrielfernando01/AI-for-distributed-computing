# ===========================================================================
# Código para imprimir en pantalla que no existe inverso multiplicativo de 0.
resultado = None
x = 10
y = 2
if y != 0:
    resultado = x / y
else:
    resultado = f'No se puede dividir {x} entre {y}'
print(resultado)
