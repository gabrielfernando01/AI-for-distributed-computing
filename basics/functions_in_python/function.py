# Funciones en Pyhon
# Dividir y organizar el código en partes más sencillas.
# Encapsular el código que se repite para ser reutilizado

# Función que muestra por pantalla el resultado de multiplicar un número por 5.
def product_by_5(number):
    print(f'{number} * 5 = {number * 5}')

print('Start the program')
product_by_5(11)
print('Next')
product_by_5(42)
print('End')

# Sentencia return
# return que no devuelve ningún valor
def cuadrado_num_par(number):
    if not number % 2 == 0:
        return
    else:
        print(number ** 2)

cuadrado_num_par(8)
cuadrado_num_par(7)

# Varios return en una misma función
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

is_even(12)
is_even(31)

# Devolver más de un valor con return en Python.
def cuadrado_cubo(number):
    return number ** 2, number ** 3

sqrt, cube = cuadrado_cubo(3)
sqrt
cube

# Se puede devolver los diferentes resultados en una lista.
def multiples_of(number):
    result = []
    for i in range(11):
        result.append(number * i)
    return result

res = multiples_of(11)
res

