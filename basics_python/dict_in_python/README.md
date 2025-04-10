![](https://raw.githubusercontent.com/gabrielfernando01/AI-for-distributed-computing/master/image/dict.png)

# dict Python - Diccionarios en Python: El tipo diccionario y operaciones más comunes 📕.

## ¿Qué es el tipo dict en Python 🐍?

La clase dict de Python es un tipo mapa que asocia claves a valores. A diferencia de los tipos secuencia (list, tuple, range, o str), que son indexados por un índice numérico, los diccionarios son indexados por claves. Estas claves siempre deben ser de un tipo inmutable, concretamente un tipo _hashable._

***
**Nota:** Un objeto es _hasheable_ si tiene un valor de hash que no cambia durante todo su ciclo de vida. En un principio, los objetos que son instancias de clases definidas por el usuario son _hasheable_. También lo son la mayoría de tipos inmutables definidos por Python (_int, float_ o _str_).
***

Piensa siempre en un diccionario como un contenedor de pares _clave: valor_, en el que la clave puede ser de cualquier tipo hasheable y es úinca en el diccionario que la contiene. Generalmente, se suelen usar como claves los tipos _int_ y _str_ aunque, como te he dicho, cualquier tipo _hasheable_ puede ser una clave.

**Las principales operaciones** que se suelen realizar con diccionarios **son almacenar un valor asociado a una clave y recuperar un valor a partir de una clave**. Esta es la esencia de los diccionarios y es aquí donde son realmente importantes. **En un diccionario, el acceso a un elemento a partir de una clave es una operación realmente rápida, eficaz y que consume pocos recursos** si lo comparamos con cómo lo haríamos con otros tipos de datos.

Otras características a resaltar de los diccionarios:

- **Es un tipo mutable**, es decir, su contenido se puede modificar después de haber sido creado.
- **Es un tipo ordenado.** Preserva el orden en que se insertan los pares _clave: valor._

### ¿Cómo crear un diccionario 📕?

En Python hay varias formas de crear un diccionario. Las veremos a continuación.

La más simple es capturar una secuencia de pares _clave: valor_ separados por comas entre llaves <code>{}</code>.

```
>>> d = {1:'hola', 89:'Pyhonista', 'a': 'b', 'c':'27'}
```

Para crear un diccionario vacío, simplemente asigna a una variable el valor <code>{}</code>.

También se puede usar el constructor de la clase <code>dict()</code> de varias maneras:

- **Sin parámetros.** Esto creará un diccionario vacío.
- Con pares _clave:valor_ dentro de llaves.
- **Con argumentos con nombre.** El nombre del argumento será la clave en el diccionario. En este caso, las claves solo pueden ser identificadores válidos y mantienen el orden en el que se indican. No se podría, por ejemplo, tener números enteros como clave.
- **Pasando un iterable.** En este caso, cada elemento del iterable debe ser también un iterable con solo dos elementos. El primero se toma como clave del diccionario y el segundo como valor. Si la clave aparece varías veces, el valor que prevalece es el último.

Los ejemplos de los casos anteriores te los comparto en el archivo: dict.py de este mismo directorio.

## ¿Cómo acceder a los elementos de un diccionario en Python?

Acceder a un elemento de un diccionario es una de las principales operaciones por las que existe este tipo de dato. El acceso a un valor se realiza mediante indexación de la clave. Para ello, simplemente captura entre corchetes la clave del elemento <code>d[clave]</code>. En caso de que la clave no exista, se lanzará la excepción <code>KeyError</code>.

![](https://raw.githubusercontent.com/gabrielfernando01/AI-for-distributed-computing/master/image/acceder_dict.png)

La clase $dict$ también ofrece el método <code>get(clave[, valor por defecto])</code>. Este método devuelve el valor correspondiente a la clave <code>clave</code>. En caso de que la clave no exista no lanza ningún error, sino que devuelve el segundo argumento $valor por defecto$. Si no se proporciona este argumento, se devuelve el valor <code>None</code>.

![](https://raw.githubusercontent.com/gabrielfernando01/AI-for-distributed-computing/master/image/get_dict.png)

## for dict Python - Recorrer un diccionario

Hay varias formas de recorrer los elementos de un diccionario: recorrer solo las claves, solo los valores o recorrer a la vez las claves y los valores. 

### Bucle for en diccionarios

Un caso en especial de bucle for se da al recorrer los elementos de un diccionario. Dado que un diccionario está compuesto por pares clave/valor, hay distintas formas de iterar sobre ellas.

![](https://raw.githubusercontent.com/gabrielfernando01/AI-for-distributed-computing/master/image/for_dict.png)

### Añadir elementos a un diccionario en Python

Como ya lo comentamos, la clase <code>dict</code> es mutable, por lo que se puede añadir, modificar y/o eliminar elementos después de haber creado un objeto de este tipo.

Para añadir un nuevo elemento a un diccionario existente, se usa el operador asignación <code>=</code>. A la izquierda del operador aparece el objeto diccionario con la nueva clave entre corchetes <code>[]</code> y a la derecha el valor que se asocia a dicha clave.

También existe el método <code>setdefault(clave[, valor])</code>. Este método devuelve el valor clave si ya existe, y en caso contrario, le asigna el valor que se pasa como segundo argumento. Si no se especifica este segundo argumento, por defecto es <code>None</code>.

![](https://raw.githubusercontent.com/gabrielfernando01/AI-for-distributed-computing/master/image/setdefault.png)

### Modificar elementos de un diccionario

Basta con asignar un nuevo valor a dicha clave del diccionario

```
>>> d = {'uno': 1, 'dos': 2}
>>> d
{'uno': 1, 'dos':2}
>>> d['uno'] = 1.0
>>> d
{'uno':1.0, 'dos':2}
```

### Eliminar un elemento de un diccionario en Python

Los diversos modos de eliminar un elemento de un diccionario. Son los siguintes:

- <code>pop(clave[, valor por defecto])</code>: Si la $clave$ está en el diccionario, elimina el elemento y devuelve su valor; si no, devuelve el _valor por defecto_. Si no proporciona el _valor por defecto_ y la _clave_ no está en el diccionario, se lanza la excepción $KeyError$
- <code>popitem()</code>: Elimina el último par _clave:valor_ del diccionario y lo devuelve. Si el diccionario está vacío se lanza la excepción $KeyError$.
- <code>del d[clave]</code>: Elimina el par $clave:valor$. Si no existe la clave, se lanza la excepción </code>KeyError</code>.
- <code>clear()</code>: Borra todos los pares <code>clave:valor</code> del diccionario.

![](https://raw.githubusercontent.com/gabrielfernando01/AI-for-distributed-computing/master/image/clear_dict.png)

## Número de elementos (len) de un diccionario en Python

Al igual que sucede con otros tipos de contenedores, se puede usar la función de Python <code>len()</code> para obtener el número de elementos de un diccionario.

```
>>> d = {'uno':1, 'dos':2, 'tres':3}
>>> len(d)
3
```

## Comprobar si un elemento está en un diccionario en Python

Al operar con diccionarios, se puede usar el operador de pertenencia <code>in</code> para comprobar si una clave está contenida, o no, en un diccionario. Esto resulta útil, por ejemplo, para asegurarnos de que una clave exista antes de intentar eliminarla.

```
>>> print('uno' in d)
True
>>> print(1 in d)
False

# Si existe la clave 1 en d, eliminala
>>> if 1 in d:
...		del d[1]
...
>>> d
{'uno':1, 'dos':2, 'tres':3}
```

## Comparar si dos diccionarios son iguales

En Python se puede utilizar el operador de igualdad <code>==</code> para comparar si dos diccionarios son iguales. **Dos diccionarios son iguales si contienen el mismo conjunto de pares clave:valor,** independientemente del orden que tengan:

![](https://raw.githubusercontent.com/gabrielfernando01/AI-for-distributed-computing/master/image/iqual_dict.png)

## Listado de métodos de la clase dict

En listamos los principales métodos de la clase _dict._

![](https://raw.githubusercontent.com/gabrielfernando01/AI-for-distributed-computing/master/image/methods_dict.png)