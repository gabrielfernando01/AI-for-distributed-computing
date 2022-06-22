![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/poo_python.png)

# Programación orientada a objetos (OOP) en Python.

Como sabrás, Python es un lenguaje multiparadigma: soporta la programación imperativa y funcional, pero también la programación orientada a objetos.

Este tutorial es un resumen de los conceptos clave de la programación orientada a objetos desde el punto de vista de Python.

## Índice

- Python es un lenguaje orientado a objetos
- Clases y objetos en Python
- Constructor de una clase en Python
- Atributos, atributos de datos y métodos
- Atributo de clase y atributos de instancia
- Herencia en Python
- Herencia múltiple en Python
- Encapsulación atributos privados
- Polimorfismo

## Python es un lenguaje orientado a objetos

**En Python todo es un objeto.** Cuando creas una variable y le asignas un valor entero, ese valor es un objeto; una función es un objeto; las listas, las tuplas, diccionarios, conjuntos, ... son objetos; una cadena de caracteres es un objeto. Y así podríamos seguir indefinidamente.

Pero, ¿por qué es tan importante la programación orientada a objetos? Bien, este tipo de programación introduce un nuevo paradigma que nos permite encapsular y aislar datos y operaciones que se pueden realizar sobre dichos datos.

## Clases y objetos en Python

Básicamente, una clase es una entidad que define una serie de elementos que determinan un estado (datos) y un comportamiento (operaciones sobre los datos que modifican su estado).

Por su parte, un objeto es una concreción o instancia de una clase.

Pensemos en el siguiente ejemplo.

Si te digo que te imagines un coche, en tu mente comienzas a visualizar la carrocería, el color, las ruedas, el volante, el combustible, el color de la tapicería, si es manual o automático, si acelera o va marcha atrás, etc.

Entonces todo lo que acabo de describir viene a ser una clase y cada uno de los coches que has imaginado, serían objetos de dicha clase.

¿Cómo pasamos lo anterior a Python? Veámoslo.

Como te decía, una clase engloba datos y funcionalidad. Cada vez que se define una clase en Python, se crea a su vez un tipo nuevo (¿recuerdas? tipo <code>int</code>, <code>float</code>, <code>str</code>, <code>list</code>, <code>tuple</code>, ... todos ellos están definidos en una clase).

Para definir una clase en Python se utiliza la palabra reservada <code>class</code>. El siguiente esquema visualiza los elementos principales que componen una clase. Todos ellos los iremos viendo con detenimiento en las siguientes secciones:

![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/class.png)

El esquema anterior define la clase <code>Coche</code> (es una versión muy, muy simplificada de lo que es un coche, jaja, pero nos sirve de ejemplo). Dicha clase establece una serie de datos, como <code>ruedas</code>, <code>color</color>, <code>aceleración</code> o <code>velocidad</code> y las operaciones <code>acelera()</code> y <code>frena()</code>.

Cuando se crea una variable de tipo <code>Coche</code>, realmente se está instanciando un objeto de dicha clase. En el siguiente ejemplo se crean dos objetos de tipo <code>Coche</code>:

```
>>> c1 = Coche('rojo', 20)
>>> print(c1.color)
rojo
>>> print(c1.ruedas)
4
>>> c2 = Coche('azul', 30)
>>> print(c2.color)
azul
>>> print(c2.ruedas)
4
```

<code>c1</code> y <code>c2</code> son objetos cuya clase es <code>Coche</code>. Ambos objetos pueden <code>acelerar</code> y <code>frenar</code>, por que su clase define estas operaciones y tienen un <code>color</code>, porque la clase <code>Coche</code> también define este _dato_. Lo que ocurre es que <code>c1</code> es de <code>color</code> _rojo_, mientras que <code>c2</code> es de <code>color</code> _azul._

**Nota:** Es una convención utilizar la notación CamelCase para los nombres de las clases. Esto es, la primera letra de cada palabra del nombre está en mayúscula y el resto de letras se mantienen en minúsculas.

## Constructor de una clase en Python.

En la sección anterior ya hemos adelantado un poco... Para crear un objeto de una clase determinada, es decir, _instanciar_ una clase, se usa el nombre de la clase y a continuación se añaden paréntesis (como si se llamará a una función).

```
obj = MiClase()
```

El código anterior crea una nueva instancia de la clase <code>MiClase</code> y asigna dicho objeto a la variable <code>obj</code>. Esto crea un objeto _vacío_, sin estado.

Sin embargo, hay clases (como nuestra clase <code>Coche</code>) que deben o necesitan crear instancias de objetos con un estado inicial.

Esto se consigue implementando el método especial <code>\_\_init\_\_</code>. Este método es conocido como el constructor de la clase y se invoca cada vez que se instancia un nuevo objeto.

El método <code>\_\_init\_\_</code> establece un primer parámetro especial que se suele llamar <code>self</code> (veremos qué significa este nombre en la siguiente sección). Pero puede especificar otros parámetros siguiendo las mismas reglas que cualquier otra función.

En nuestro caso, el constructor de la <code>Coche</code> es el sigiente:

```
def __init__(self, color, aceleracion):
    self.color = color
    self.aceleracion = aceleracion
    self.velocidadd = 0
```

Como puedes observar, además del parámetro <code>self</code>, define los parámetros <code>color</code> y <code>aceleracion</code>, que determinan el estado inicial de un objeto de tipo <code>Coche</code>.

En este caso, para instanciar un objeto de tipo coche, debemos pasar como argumento el color y la aceleración como vimos en el ejemplo:

```
c1 = Coche('rojo', 20)
```

**IMPORTANTE:** A diferencia de otros lenguajes, en los que está permitido implementar más de un constructor, en Python solo se puede definir un método <code>\_\_init\_\_()</code>.

## Atributos, atributos de datos y métodos.

Una vez que sabemos qué es un objeto, tengo que decirte que la única operación que pueden realizar los objetos es referenciar a sus atributos por medio del operador <code>.</code>

Como habrás podido apreciar, un objeto tiene dos tipos de atributos: _atributos de datos_ y _métodos._

- Los atributos de datos definen el estado del objeto. En otros lenguajes son conocidos simplemente como atributos o miembros.
- Los métodos son las funciones definidas dentro de la clase.

Siguiendo con nuestro ejemplo de la clase <code>Coche</code>, vamos a crear el siguiente objeto:

```
>>> c1 = Coche('rojo', 20)
>>> print(c1.color)
rojo
>>> print(c1.velocidad)
0
>>> c1.acelera()
>>> print(c1.velocidad)
20
```

En la segunda línea del código anterior, el objeto <code>c1</code> está referenciando  al atributo de dato <code>color</code> y en la cuarta línea al atributo <code>velocidad</code>. Sin embargo, en la sexta línea se referencia al método <code>acelera()</code>. Llamar a este método tiene una implicación como puedes observar y es que modifica el estado del objeto, dado que se incrementa su velocidad. Este hecho lo puedes apreciar cuando se vuelve a referenciar al atributo <code>velocidad</code> en la séptima línea.

### Atributos de datos.

A diferencia de otros lenguajes, los atributos de datos no necesitan ser declarados previamente. Un objeto los crea del mismo modo en que se crean las variables en Python, es decir, cuando les asigna un valor por primera vez.

El siguiente código es un ejemplo de ello:

```
>>> c1 = Coche('rojo', 20)
>>> c2 = Coche('azul', 10)
>>> print(c1.color)
rojo
>>> print(c2.color)
azul
>>> c1.marchas = 6
>>> print(c1.marchas)
6
>>> print(c2.marchas)
Traceback(most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'Coche' object has no attribute 'marchas'.
```

