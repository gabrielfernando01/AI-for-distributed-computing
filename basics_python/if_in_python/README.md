![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/if_header.png)

# Python if - Sentencia if de control de flujo.

En Python if es una de las principales sentencias de control de flujo, junto a while y for.

## Python if - Sentencia básica

En Python, la sentencia if se utiliza para ejecutar un bloque de código si, y solo si, se cumple una determinada condición. Por tanto, if es usado para la toma de decisiones.

La estructura básica de esta sentencia if es la siguiente:

```
if condicion:
	bloque de código
```

Es decir, solo si la <code>condicion</code> se evalúa a <code>True</code>, se ejecutarán las sentencias que forman parte de <code>bloque de código</code>. En caso de que se evalúe a <code>False</code> no se ejecutará ninguna sentencia perteneciente a <code>bloque de codigo</code>.

***
**¡Importante!:** El cuerpo del bloque está indicado con un sangrado mayor. Dicho bloque termina cuando se encuentre la primera línea con un sangrado menor.
***

Veamos un ejemplo:

```
x = 17
if x < 20:
    print('x es menor que 20')
```

En el código anterior la variable <code>x</code> toma el valor de <code>17</code>. En la segunda línea, la sentencia <code>if</code> evalúa si <code>x es menor que 20</code>. Como el valor devuelto por la expresión es <code>True</code>, se ejecuta el bloque <code>if</code>, mostrando por consola la cadena <code>x es menor que 20</code>.

Veamos otro ejemplo:

```
valores = [1, 3, 4, 8]
if 5 in valores:
    print('está en valores')
print('fin')
```

En este caso tenemos una lista de <code>valores</code>. El if comprueba si el número <code>5</code> se encuentra entre estos <code>valores</code>. Como la expresión devuelve como resultado <code>False</code>, porque <code>5</code> no está entre los <code>valores</code>, el código anterior simplemente mostrará por pantalla la cadena <code>fin</code>.

***
**¡RECUERDA!:** En principio, en Python todos los objetos/instancias se evalúan a <code>True</code> a excepción de <code>None</code>, <code>False</code>, <code>0</code> de todos los tipos numéricos y secuencias/colecciones vacías, que se evalúan a <code>False</code>.
***

## Sentencia if ... else.

Hay ocasiones en que la sentencia <code>if</code> básica no es suficiente y es necesario ejecutar un conjunto o sentencias cuando la condición se evalúa a <code>False</code>.

Para ello se utilisa la estructura <code>if ... else ...</code> Como lo expreso a continuación.

```
if condición:
    bloque de código (cuando condición se evalúa a True)
else:
    bloque de código 2 (cuando condición se evalúa a False)
```

Imagina que estás implementando un programa en el que necesitas realizar la división de dos números. Si divides un número entre 0, el programa lanzará un error y terminará. Para evitar esto, escribimos un pequeño script de nombre: inverso_mult.py que te lo comparto en esta misma carpeta, le código es el siguiente:

```
resultado = None
x = 10
y = 2
if y != 0:
    resultado = x / y
else:
    resultado = f'No se puede dividir {x} entre {y}'
print(resultado)
```

## if ... elif ... else

Es posible que te encuentres en situaciones en que una decisión dependa de más de una condición. En este caso se usa una sentencia if compuesta, cuya estructura es la siguiente:

```
if cond1:
    bloque cond1 (sentencias si se evalúa la cond1 a True)
elif cond2:
    bloque cond2 (sentencias si cond1 es False pero cond2 es True)
...
else:
    bloque else (sentencias si todas las condiciones se evalúan a False)
```

Es decir, en esta ocasión, se comprueba la condición <code>cond1</code>. Si se evalúa a <code>True</code>, se ejecuta el bloque <code>bloque cond1</code> y después el flujo continúa después del bloque if.

Sin embargo, <code>cond1</code> se evalúa a <code>False</code>, se comprueba la <code>cond2</code>. Si esta se evalúa a <code>True</code>, se ejecutara el bloque de sentencias <code>bloque cond2</code>. En caso contrario, pasaría a comprobar la condición del siguiente <code>elif</code> y así sucesivamente hasta que llegue al <code>else</code>, que se ejecuta si ninguna de las condiciones anteriores se evaluaron a <code>True</code>.

Veamos un ejemplo. Imagina que queremos comprobar si un número es menor que 0, igual a 0, o mayor que 0 y en cada situación debemos ejecutar un código diferente. En este caso, hacemos uso de la estructura if ... elif ... else anterior:

```
x = 28
if x < 0:
    print(f'{x} es menor que 0')
elif x > 0:
    print(f'{x} es mayor que 0')
else:
    print('x es 0')
```

## Sentencias if anidadas

Para los casos anteriores es importante saber que se puede volver a inclur una sentencia if, o if ... else ... o if ... elif ... else ...

Como se puede ver en este ejemplo:

```
x = 28
if x < 0:
    print(f'{x} es menor que 0')
else:
    if x > 0:
        print(f'{x} es mayor que 0')
    else:
        print('x es 0')
```
