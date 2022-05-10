# list Python
# Una lista puede contener elementos compuestos, objetos u otros listas:
lista = [1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola']

# El tipo str también es un tipo secuencia. Si pasamos un string al 
# constructor list() creará una lista cuyos elementos son cada uno de 
# los caracteres de la cadena:
vowels = list['aeiou']
vowels

# Dos alternativas para crear listas vacias:
lista_1 = []
lista_2 = list()

# Acceder a los elementos de una lista dentro de otra lista, usando indices
# compuestos o anidados.
lista = ['a', ['d', 'b'], 'z']
lista[1][1]

# Acceso usando índice negativo
vowels[-1]

# Acceso a un subconjunto de elementos utilizando rangos en los índices.
vowels[2:3]     # Elementos desde el 2 hasta el índice 3-1
vowels[2:4]     # Elementos desde el 2 hasta el índice 4-1
vowels[:]       # Todos los elementos
vowels[1:]      # Elementos desde el índice 1
vowels[:3]      # Elementos hasta el índice 3-1

# Acceso a los elementos de una lista indicando un paso con el operador [::]
letters = list('abcdefghsjk')
letters[::2]    # Acceso a los elementos de 2 en 2
letters[1:5:2]  # Elementos del 1 al 4 de 2 en 2
letters [1:6:3] # Elementos del 1 al 5 de 3 en 3

# for list Python
colors = ['blue', 'red', 'orange']
for color in colors:
    print(color)

# Para añadir un nuevo elemento a una lista se utiliza el método append()
# y para añadir varios elementos, el método extend()
vowels = ['a']
vowels.append('e')                  # Añade un elemento
vowels.extend(['i', 'o', 'u'])      # Añade un grupo de elementos

# Usar el operador de concatenación + para unir dos listas en una sola. 
list1 = [1, 2, 3]
list2 = [3, 1, 5]
new_list = list1 + list2
new_list

# El operador * repite el contenido de una lista n veces:
numbers = [7, 8, 12]
numbers *= 3
numbers

# Añadir un elemento en una posición concreta de una lista con el método
# insert(index, element). Los elementos cuyo índice sea mayor a index se
# desplazaran una posición a la derecha.
vowels = ['a', 'e', 'o', 'u']
vowels.insert(2, 'i')
vowels

# Modificar elementos de una lista
vowels = ['o', 'o', 'e', 'o', 'o']

# Actualizar el elemento del índice 0
vowels[1] = 'e'

# Actualizar los elementos entre las posiciones 2 y 3
vowels[2:4] = ['i', 'o']

# Con la sentencia del se puede eliminar un elemento a partir de su indice
# Eliminar el elemento del índice 2
vowels = list('aeiou')
del vowels[2]
vowels

# Eliminar los elementos con índices 2 y 3.
vowels = list['aeiou']
del vowels[2:4]
vowels

# Eliminar todos los elementos
vowels = list['aeiou']
del vowels[2:4]
vowels

# Elimina la primera ocurrencia del carácter e
letters = list('kvfesd')
letters.remove('e')
letters

# Obtiene y elimina el último elemento
letters.pop()
letters

# Eliminar todos los elementos de una lista a través del método clear():
letters = ['a', 'b', 'c']
letters.clear()
letters

# Devolver el número de elementos de una lista:
vowels = list('aeiou')
len(vowels)

# Saber si un elemento se encuentra dentro de una lista
vowels = list('aeiou')
if 'a' in vowels:
    print('a is in vowels')

if 'b' not in vowels:
    print('b not is in vowels')

# Lista desordenada de números enteros
numbers = list('8343847')

# Identidad del objeto número 
id(numbers)

# Se llama al método sort() para ordenar los elementos de la lista
numbers.sort()
numbers

# Se comprueba que la identidad del objeto numbers es la misma
id(numbers)


