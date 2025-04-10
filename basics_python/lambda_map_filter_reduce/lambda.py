# Las funciones lambdas son también conocidas como funciones anónimas porque
# se definen sin un nombre

# La sintaxis para definir una función lambda es la siguiente:
lambda parámetros: expresión

# Estas funciones están restringidas a una sola expresión
# Se suelen usar en combinación con otras funciones, generalmente como 
# argumentos de otra función.

# Ejemplo
sqrt = lambda x: x ** 2

# Diferencia y similitudes al usar lambda y una función tipica.
def cuadrado(x):
    return x ** 2

sqrt = lambda x: x ** 2

print(cuadrado(3))
print(sqrt(5))

# Ejemplos de uso comunes de funciones lambda: map(), filter(), y reduce().
# map() aplica una función a cada uno de los elementos de una lista.
map(una_funcion, una_lista)

# Si tenemos una lista de enteros y queremos el cuadrado de cada uno, entonces:
integers = [1, 2, 3, 5, 12]
sqrts = []
for e in integers:
    sqrts.append(e ** 2)

print(sqrts)













