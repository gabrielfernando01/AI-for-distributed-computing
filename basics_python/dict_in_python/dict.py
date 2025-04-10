# ==========================================================
# Creación de diccionarios
# Pares clave:valor entre llaves
d = {'uno':1, 'dos':2, 'tres':3}
d

# Argumentos con nombre
d2 = dict(uno=1, dos=2, tres=3)
d2

# Pares clave:valor entre llaves
d3 = dict({'uno':1, 'dos':2, 'tres':3})
d3

# Iterable que contiene iterables con dos elementos
d4 = dict([('uno':1), ('dos':2), ('tres':3)])
d4

# Diccionario vacío
d5 = {}
d5

# Diccionario vacío usando el contructor
d6 = dict()
d6

# ===========================================================
# Cómo acceder a los elementos de un diccionario en Python
d = {'uno':1, 'dos':2, 'tres':3}
d['dos']
d['cuatro']

# Método get(clave[, valor por defecto])
d = {'uno':1, 'dos':2, 'tres':3}
d.get('uno')

# Devuelve 4 como valor por defecto si no encuetra la clave
d.get('cuatro', 4)

# Devuelve None como valor por defecto si no encuentra la clave
a = d.get('cuatro')
a
type(a)

# =============================================================
# Bucle for en diccionarios:
# Recorrer las claves de un diccionario.
values = {'A':4, 'E':3, 'I':1, 'O':0}
for k in values:
    print(k)

# Iterar sobre los valores del diccionario
values = {'A':4, 'E':3, 'I':1, 'O':0}
for v in values.values():
    print(v)

# Iterar a la vez sobre la clave y el valor de cada uno de los elementos
# del diccionario
values = {'A':4, 'E':3, 'I':1, 'O':0}
for k, v in values.items():
    print('k =', k, ' v=', v)

# ===============================================================
# Añadir elementos a un diccionario en Python
d = {'uno':1, 'dos':2}
d

# Añade un nuevo elemento al diccionario
d['tres'] = 3
d

# ===============================================================
# Método setdefault(clave[, valor])
d = {'uno':1, 'dos':2}
d.setdefault('uno', 1.0)

d.setdefault('tres', 3)

d.setdefault('cuatro')
d


# ===============================================================
# Eliminar un elemento de un diccionario
d = {'uno':1, 'dos':2, 'tres':3, 'cuatro':4, 'cinco':5}

# Elimina un elemento con pop()
d.pop('uno')
d

# Elimina una elemento con popitem()
d.popitem()
d

# Elimina un elemento con del
del d['tres']
d

# Elimina todos los elementos del diccionario
d.clear()
d


# ===============================================================
# Comparar si dos diccionarios son iguales
d1 = {'uno':1, 'dos':2}
d2 = {'dos':2, 'uno':1}
d3 = {'uno':1}
print(d1==d2)

print(d1==d3)

# Otro tipo de comparador no está permitido en diccionarios
print(d1 > d2)

