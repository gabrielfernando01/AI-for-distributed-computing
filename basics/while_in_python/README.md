![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/while_header.png)

# While Python - Bucle while en Python

La sentencia o bucle while en Python es una sentencia de control de flujo que se utiliza para ejecutar un bloque de instrucciones de forma continua mientras se cumpla una condición determinada.


## La sentencia while en Python

El uso principal de la sentencia _while_ es ejecutar repetidamente un bloque de código **mientras** se cumple una condición.

La estructura de la sentencia es la siguiente:

```
while condicion:
    bloque de código
```

Es decir, mientras <code>condición</code> se evalúe a <code>True</code>, se ejecutarán las instrucciones y sentencias de <code>bloque de código</code>.

Aquí, <code>condición</code> puede ser un literal, el valor de una variable, el resultado de una expresión o el valor devuelto por una función.

***
**¡IMPORTANTE!:** El cuerpo del bloque while está indicado con una sangría mayor. Dicho bloque termina cuando se encuentre la primera línea con un sangrado menor.
***

En el siguiente gif te muestro como imprimir los primeros 10 múltiplos de <code>11</code>, es decir, en educación básica nos dirian, la tabla del 11 de los primeros 10 números:

![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/multiples.gif)

## Bucle while en Python

Un ejemplo típico del uso del bucle while es: Comprobar si existe un elemento en una secuencia.

***
**¡Nota!:** El ejemplo ocupado en while.py es solo un ejemplo para hacer notar como funciona la sentencia while. La manera más eficiente de comprobar si un elemento pertenece a una lisa es con el operador in.
***

## Bucle while ... else ...

Al igual que ocurre con el bucle for, podemos alterar el flujo de ejecución del bucle while con las sentencias break y continue:

- break se utiliza para finalizar y salir del bucle, por ejemplo, si cumple una condición.
- Por su parte, continue salta al siguiente paso de la iteración, ignorando todas las sentencias que le siguen y que forman parte del bucle.