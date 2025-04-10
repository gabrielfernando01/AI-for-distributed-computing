![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/header_operation.png)

# Operadores en Python

Los ejemplos de este tema están en el fichero: operators.py de esta misma carpeta.

Los operadores son símbolos reservados por el propio lenguaje que se utiliza para llevar a cabo operaciones sobre uno, dos o más elementos. Estos objetos pueden ser variables, literales, el valor devuelto por una expresión o el valor devuelto por una función.

El ejemplo más típico que siempre viene a la mente es el operador suma, <code>+</code>, que se utiliza para obtener la suma aritmética de dos variables:

```
>>> 9 + 1
10
```

## Operador de concatenación de cadenas de caracteres

La forma más simple de concatenar dos cadenas en Python es utilizando el operador de concatenación <code>+</code>.

```
>>> hola = 'Hola'
>>> python = 'Pythonista'
>>> hola_python = hola + ' ' + python
>>> print(hola_python)
Hola Pythonista
```

## Operadores lógicos o booleanos

A la hora de operar con valores booleanos, tenemos a nuestra disposición los operadores <code>and</code>, <code>or</code>, <code>not</code>.

***
**IMPORTANTE:** Las operaciones <code>and</code>, <code>or</code> y <code>not</code> realmente no devuelven <code>True</code> o <code>False</code>, sino que devuelven uno de los elementos operados como vemos enseguida.
***

![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/operation.png)

Ejemplos:

```
>>> x = True
>>> y = False
>>> x or y
True

>>> x and y
False

>>> x = 0
>>> y = 10
>>> x or y
10

>>> x and y
0

>>> not x
True
```

## Operadores de comparación

Los operadores de comparación se utilizan, como su nombre lo indica, para comparar dos o más valores. El resultado de estos 

![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/comparacion.png)

Ejemplos:

```
>>> x = 0
>>> y = 1
>>> y < y
False
>>> x > y
True
>>> x == y
False
```

## Operadores aritméticos en Python.

Los operadores aritméticos en Python son los siguintes:

![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/aritmeticos.png)

```
>>> x = 7
>>> y = 2
>>> x + y  # suma
9
>>> x - y  # resta
5
>>> x * y  # producto
14
>>> x / y  # división real
3.5
>>> x % y  # resto
1
>>> x // y  # cociente entero
3
>>> x ** y  # potenciación
49
```

## Operadores a nivel bits

Los operadores a nivel bit actúan sobre los operandos como si fueran una cadena de dígitos binarios. Como su nombre lo indica, actúan sobre los operandos bit a bit. Son los siguientes.

![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/bit.png)

Supongamos que tenemos el entero 2 (en bits es 00010) y el entero 7 (00111).

```
>>> x = 2
>>> y = 7
>>> x | y
7
>>> x ^ y
5
>>> x & y
2
>>> x << 1
4
>>> x >> 1
1
>>> ~x
-3
```


## Operadores de asignación

El operador de asignación es <code>=</code>, y sirve para asignar un valor a una variable.

Existen otros operadores de asignación compuestos que realizan una operación básica sobre la variable a la que se le asigna el valor.

Por ejemplo, <code>x += 1</code> es lo mismo que <code>x = x + 1</code>. Los operadores compuestos realizan la operación que hay antes del signo igual, tomando como operandos la propia variable y el valor a la derecha del signo igual.

![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/asignacion.png)

## Operadores de pertenencia

Los operadores de pertenencia se utilizan para comprobar si un valor o variable se encuentra en una secuencia (<code>list</code>, <code>tuple</code>, <code>dict</code>, <code>set</code>, o <code>str</code>).

![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/pertenencia.png)

## Operadores de identidad

Los operadores de identidad se utilizan para comprobar si dos variables son, o no, el mismo objeto.

![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/identidad.png)

***
**Recuerda:** Para conocer la identidad de un objeto se usa la función id().
***

```
>>> x = 4
>>> y = 2
>>> lista = [1, 5]
>>> x is lista
False
>>> x is y
False
>>> x is 4
True
```

## Prioridad de los operadores en Python

Al igual que ocurre en las matemáticas, los operadores en Python tienen un orden de prioridad. Este orden es el siguiente, de menos prioritario a más prioritario: operadores booleanos, operadores de comparación, identidad y pertenencia; a nivel de bits y finalmente los aritméticos (con el mismo orden de prioridad que en las matemáticas).

Este orden de prioridad se puede alterar con el uso de los paréntesis <code>()</code>:

```
>>> x = 5
>>> y = 2
>>> z = x + 3 * y  # El producto tiene prioridad sobre la suma
>>> z
11
>>> z = (x + 3) * y  # Los paréntesis tienen prioridad
>>> z
16
```