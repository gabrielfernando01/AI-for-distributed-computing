![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/for.png)

# for en Python

El ciclo for se utiliza para recorrer los elementos de un objeto _iterable_ (lista, tupla, conjunto, diccionario,...) y ejecutar un bloque de código. En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, sobre el cual se puede aplicar una serie de operaciones.

La sintaxis es la siguiente:

```
for <elem> in <iterable>:
    <Tu codigo>
```

Aquí <code>elem</code> es la variable que toma el valor del elemento dentro del iterador en cada paso del bucle. Este finaliza su ejecución cuando se recorren todos los elementos.

Es muy común usar un bucle for para iterar sobre los elementos de listas, tuplas o diccionarios.

**Ejemplo**

Si tenemos una lista de números y queremos imprimirlos en consola:

```
nums = [4, 78, 9, 84]
for n in nums:
    print(n)

4
78
9
84
```

## ¿Que es un iterable?

Un _iterable_ es un objeto que permite recorrer sus elementos uno a uno. Para ser más técnico, un objeto iterable es aquél que puede pasarse como parámetro de la función <code>iter()</code>.

Esta función devuelve un iterador basado en el objeto iterable que se pasa como parámetro.

Finalmente, un _iterador_ es un objeto que define un mecanismo para recorrer los elementos del iterable asociado.

**Ejemplo**

```
>>> nums = [4, 78, 9, 84]
>>> it = iter(nums)
>>> next(it)
4
>>> next(it)
78
>>> next(it)
9
>>> next(it)
84
>>> next(it)
Traceback (most recent call last):
File "<input>", line 1, in <module>
StopIteration
```

Como puedes observar, un _iterador_ recorre los elementos de un _iterable_ solo hacia delante. Cada vez que se llama a la función <code>next()</code> se recupera el siguiente valor del _iterador_. 

En Python, los tipos principales <code>list</code>, <code>dict</code>, <code>set</code>, o <code>string</code> entre otros, son iterables, por lo que podrán ser usados en el bucle for.

## Bucle for en diccionarios

Un caso en especial de bucle for se da al recorrer los elementos de un diccionario. Dado que un diccionario está compuesto por pares clave/valor, hay distintas formas de iterar sobre ellas.

Recorrer las claves del diccionario:

```
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k in valores:
    print(k)

A
E
I
O
```

Iterar sobre los valores del diccionario

```
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for v in valores.values():
    print(v)

4
3
1
0
```

Iterar a la vez sobre la clave y el valor de cada uno de los elementos del diccionario.

```
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k, v in valores.items():
    print('k=', k, ', v=', v)

k=A, v=4
k=E, v=3
k=I, v=1
k=O, v=0
```

## Python for y la clase range

¿Cómo implementamos y/o simulamos en Python el bucle for basado en una secuencia numérica? Para estos casos, Python pone a nuestra disposición la clase <code>range</code>. El contructor de esta clase, <code>range(max)</code>, devuelve un iterable cuyos valores van desde <code>0</code> hasta <code>max-1</code>.

```
for i in range(11):
    print(i)

0
1
2
3
...
10
```