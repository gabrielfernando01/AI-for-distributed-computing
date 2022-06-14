![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/while_header.png)

# While Python - Bucle while en Python

La sentencia o bucle <code>while</code> en Python es una sentencia de control de flujo que se utiliza para ejecutar un bloque de instrucciones de forma continua mientras se cumpla una condición determinada.


## La sentencia while en Python

El uso principal de la sentencia <code>while</code> es ejecutar repetidamente un bloque de código **mientras** se cumple una condición.

La estructura de la sentencia es la siguiente:

```
while condicion:
    bloque de código
```

Es decir, mientras <code>condición</code> se evalúe a <code>True</code>, se ejecutarán las instrucciones y sentencias de <code>bloque de código</code>.

Aquí, <code>condición</code> puede ser un literal, el valor de una variable, el resultado de una expresión o el valor devuelto por una función.

***
**¡IMPORTANTE!:** El cuerpo del bloque <code>while</code> está indicado con una sangría mayor. Dicho bloque termina cuando se encuentre la primera línea con un sangrado menor.
***

En el siguiente gif te muestro como imprimir los primeros 10 múltiplos de <code>11</code>, es decir, en educación básica nos dirían, la tabla del 11 de los primeros 10 números:

![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/multiples.gif)

## Bucle while en Python

Un ejemplo típico del uso del bucle <code>while</code> es: Comprobar si existe un elemento en una secuencia.

Imagina que tienes la siguiente lista de valores <code>[5, 1, 9, 2, 7, 4]</code> y quieres saber si el número 2 está contenido en dicha lista. El código con la sentencia <code>while</code> es el siguiente:

```
valores = [5, 1, 9, 2, 7, 4]

encontrado = False
indice = 0
longitud = len(valores)
while not encontrado and indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
    else:
        indice += 1
if encontrado:
    print(f'El número 2 ha sido encontrado en el índice {indice}')
else:
    print('El número 2 no se encuentra en la lista de valores')
```

El anterior script lo guardo con el nombre: encontrar.py

Observemos que en el script anterior se utilizan 3 variables de control:

- <code>encontrado</code>: Indica si el número 2 ha sido encontrado en la lista.
- <code>indice</code>: Contiene el índice del elemento de la lista <code>valores</code> que va ser evaluado.
- <code>longitud</code>: Indica el número de elemento de la lista <code>valores</code>.

***
**¡Nota!:** El ejemplo ocupado en while.py es solo un ejemplo para hacer notar como funciona la sentencia <code>while</code>. La manera más eficiente de comprobar si un elemento pertenece a una lisa es con el operador <code>in</code>.
***

## Bucle while ... else ...

Al igual que ocurre con el bucle <code>for</code>, podemos alterar el flujo de ejecución del bucle <code>while</code> con las sentencias <code>break</code> y <code>continue</code>:

- <code>break</code> se utiliza para finalizar y salir del bucle, por ejemplo, si cumple una condición.
- Por su parte, <code>continue</code> salta al siguiente paso de la iteración, ignorando todas las sentencias que le siguen y que forman parte del bucle.

Retomamos el ejemplo anterior modificado, añadiendo la sentencia <code>break</code>:

```
valores = [5, 1, 9, 2, 7, 4]

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
	print('El elemento 2 no se encuentra en la lista de valores')
```