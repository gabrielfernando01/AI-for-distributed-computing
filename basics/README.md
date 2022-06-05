![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/header_basics.png)

# Basics in Python

Este pequeño tutorial pretende tocar algunos puntos para que te inicialices en este potente lenguaje. Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código, se utiliza para desarrollar aplicaciones de todo tipo, ejemplos: Instagram, Netflix, Spotify, Panda 3D, entre otros. Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, porgramación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinánico y multiplataforma.

Administrado por Python Software Foundation, posee una licencia de código abierto, denominada Python Software Foundtion License. Python se clasifica constantemente como uno de los lenguajes de programación más populares.

## Breve historia

<img align='right' src="https://serespensantes.com/wp-content/uploads/2019/04/guido-van-rossum.jpg" width="230">
Python fue creado a finales de los años ochenta por Guido van Rossum en el Centro para las Matemáticas y la informática, en los Países Bajos, como un sucesor del lenguaje de programación ABC, capaz de manejar excepciones e interactuar con el sistema operativo Amoeba.

El nombre del lenguaje proviene de la afición de su creador por los humoristas británicos Monty Python.

Python alcanzo la versión 1.0 en enero de 1994. Una característica de este lanzamiento fueron las herramientas de la programación funcional: <code>lambda</code>, <code>reduce</code> y <code>map</map>. Van Rossum explicó que \<\<hace 12 años, Python adquirió lambda, reduce(), filter() y map, cortesía de Amrit Perm, un hacker inforfático de Lisp que las implementó porque las extrañaba\>\>.

La útlima versión liberada proveniente de CWI fue Python 1.2. En 1995, van Rossum continuó su trabajo en Python en la Corporation for National Research Initiatives (CNRI) en Reston, Virginia, donde lanzó varias versiones del software.

## Contenido

En este tutorial te comparto la siguiente lista de tópicos:

- <a href="https://bsystems.com.mx/nosotros.html">Operadores en Python</a>






# Python if - Sentencia if de control de flujo.

## Pytho if - Sentencia básica

La estructura básica de esta sentencia if es la siguiente:

```
if condicion:
	bloque de código
```

Es decir, solo si la $condición$ se evalúa a $True$, se ejecutarán las sentencias que forman parte de $bloque de código$. En caso de que se evalúe a $False$ no se ejecutará ninguna sentencia perteneciente a $bloque de código$.

***
**¡Importante!:** El cuerpo del bloque está indicado con un sangrado mayor. Dicho bloque termina cuando se encuentre la primera línea con un sangrado menor.
***

***
**¡RECUERDA!:** En principio, en Python todos los objetos/instancias se evalúan a True a excepción de None, False, 0 de todos los tipos numéricos y secuencias/colecciones vacías, que se evalúan a False.
***

## Sentencia if ... else.

Hay ocasiones en que la sentencia if básica no es suficiente y es necesario ejecutar un conjunto o sentencias cuando la condición se evalúa a False.

## if ... elif ... else

Es posible que te encuentres en situaciones en que una decisión dependa de más de una condición. En este caso se usa una sentencia if compuesta.

# While Python 

La sentencia o bucle while en Python es una sentencia de control de flujo que se utiliza para ejecutar un bloque de instrucciones de forma continua mientras se cumpla una condición determinada.

Es decir, mientras 'condición' se evalúe a 'True', se ejecutarán las instrucciones y sentencias de 'bloque de código'.

Aquí, condición puede ser un literal, el valor de una variable, el resultado de una expresión o el valor devuelto por una función.

***
**¡IMPORTANTE!:** El cuerpo del bloque while está indicado con una sangría mayor. Dicho bloque termina cuando se encuentre la primera línea con un sangrado menor.
***

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

# for en Python

El ciclo for se utiliza para recorrer los elementos de un objeto _iterable_ (lista, tupla, conjunto, diccionario,...) y ejecutar un bloque de código. En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, sobre el cual se puede aplicar una serie de operaciones.

## ¿Que es un iterable?

Un _iterable_ es un objeto que permite recorrer sus elementos uno a uno. Para ser más técnico, un objeto iterable es aquél que puede pasarse como parámetro de la función iter().

## Bucle for en diccionarios

Un caso en especial de bucle for se da al recorrer los elementos de un diccionario. Dado que un diccionario está compuesto por pares clave/valor, hay distintas formas de iterar sobre ellas.
