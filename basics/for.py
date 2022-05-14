# El bucle for en Python
# for se utiliza para recorrer los elementos de un objeto iterable (lista,
# tupla, conjunto, diccionario, ...) y ejecutar un bloque de código.
# Su sintaxis es la siguiente:
for <elem> in <iterable>:
    <Your code>

# Para imprimir una lista de números en la consola.
num = [5, 3, 2, 100, 2]
for n in num:
    print(n)

# Un iterable es un objeto que se puede iterar sobre él, ie, que permite
# recorrer sus elementos uno a uno. Un objeto iterable es aquél que puede
# pasarse como parámetro de la función iter().
num = [4, 3, 7, 0, 13]
it = iter(num)
next(it)
next(it)

# En Python, los tipos principales: list, tuple, dict, set o string entre
# otros, son iterables, por lo que podrán ser usados en el bucle for.

# Un diccionario está compuesto por pares clave/valor.
values = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k in values:
    print(k)




