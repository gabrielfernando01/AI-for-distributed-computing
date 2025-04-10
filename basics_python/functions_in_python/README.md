![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/funciones.png)

# Funciones en Python

Las funciones en Python, y en cualquier lenguaje de programación, son estructuras esenciales de código. Una función es un grupo de instrucciones que constituyen una unidad lógica del programa y resuelven un problema muy concreto.

## ¿Qué son las funciones en Python?

Las funciones en Python constituyen unidades lógicas de un programa y tienen un doble objetivo:

- Dividir y organizar el código en partes más sencillas.
- Encapsular el código que se repite a lo largo de un programa para ser reutilizado.

Sabemos que Python ya define un conjunto de funciones que podemos usar directamente en nuestros códigos. Ejemplo de alguna de ellas son; la función <code>len()</code>, que obtiene el número de elementos de un objeto contenedor como una lista, una tupla, un diccionario. Otra función definida es <code>print()</code>, que muestra por consola un texto.

Aunque, usted como programador, deberás definir tus propias funciones para estructurar el código de manera que sea más legible y para reutilizar aquellas partes que se repiten a lo largo de una aplicación. 

## ¿Comó definir una función en Python?

La siguiente imagen muestra el esquema de una función en Python:

![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/def_function.png)

Para definir una función en Python se utiliza la palabra reservada <code>def</code>. A continuación viene el nombre o identificador de la función que es el que se utiliza para invocarla. Después del nombre hay que incluir los paréntesis y una lista opcional de parámetros. Además, la cabecera o definición de la función termina con dos puntos.

Tras los dos puntos <code>:</code> se incluye el cuerpo de la función (con sangrado mayor, generalmente cuatro espacios) que es el conjunto de instrucciones que se encapsulan en dicha función y que le dan significado.

Al final y de manera opcional, se añade la instrucción con la palabra reservada <code>return</code> para devolver un resultado.

***
**NOTA:** Cuando la primera instrucción de una función es un <code>string</code> encerrado entre tres comillas simple <code>'''</code> o dobles <code>"""</code>, a dicha instrucción se le conoce como <code>docstring</code>. El _docstring_ es una cadena que se utiliza para documentar la función, es decir, indicar qué hace dicha función.
***

## ¿Comó usar o llamar a una función?

Para usar o invocar una función, simplemente hay que escribir su nombre como si de una instrucción más se tratara. Y, pasar los argumentos necesarios con los que se haya definido la función.

**Ejemplo.** Creamos el siguiente script con nombre: mult_por_5.py

```
def multiplica_por_5(numero):
    print(f'{numero} * 5 = {numero*5}')

print('Comienzo del programa')
multiplica_por_5(7)
print('Siguiente')
multiplica_por_5(113)
print('Fin')
```

La función <code>multiplica_por_5()</code> define un parámetro llamado <code>numero</code> que es el que se utiliza para ejecutar la función. Debes obtener un resultado similar al siguiente:

![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/mult_5.png)

Como puedes observar, el programa comienza su ejecución en la línea <code>print('Comienzo del programa')</code> y va ejecutando las instrucciones una a una de manera ordenada. Cuando se encuentra el nombre de la función <code>multiplica_por_5</code>, el flujo de ejecución para a la primera instrucción de la función <code>print(f'{nuero} * 5 = {numero * 5}')</code>. Una vez que se ejecuta la(s) instrucción(es) de la función, el flujo del programa continua en el punto donde se quedo.

***
**¡IMPORTANTE!:** Diferencia entre **parámetro** y **argumento.** La función <code>multiplica_por_5()</code> define un _parámetro_ llamado <code>numero</code>. Sin embargo, cuando desde el código se invoca a la función, por ejemplo <code>multiplica_por_5(7)</code>, se dice que se llama a multiplicar por cinco el _argumento_ <code>7</code>.
***



