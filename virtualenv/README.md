![](https://raw.githubusercontent.com/gabrielfernando01/basics_in_python/master/image/virtualenv.png)

# virtualenv y pip - Instalando librerías en un entorno virtual Python

**virtualenv es una herramienta que nos permite tener entornos Python totalmente separados y aislados,** de manera que el intérprete y las librerías de proyectos diferentes no entren en conflicto.

## ¿Por qué es una buena práctica usar virtualenv?

Cuando estás desarrollando varios proyectos Python en un mismo ordenador, es posible que tengas más de un intérprete de Python instalado, por ejemplo, Python 2.7 y Python 3.6. Además, puede que en dos proyectos distintos hagas uso de una misma librería pero uses una versión diferente en cada uno de ellos.

¿Comó haces para que dichas librerías no entren en conflicto? Imaginemos que tenemos dos proyectos llamados <code>A</code> y <code>B</code> y que ambos hacen uso de una misma librería <code>lib_x</code>. El proyecto <code>A</code> enlaza con la versión <code>1.0.0</code> de la librería <code>lib\_x</code> y el proyecto <B>, por una serie de requisitos, utiliza nuevas funcionalidades de la librería <code>lib\_x</code> que están recogidas en las versión <code>2.0.0</code>.

Inicialmente no es posible mantener ambas versiones de la misma librería instaladas en el sistema, o se usa la versión <code>1.0.0</code> o la <code>2.0.0</code>. Es aquí donde entra en juego <code>virtualenv</code>. **Con virtualenv podemos tener entornos Python de configuración y ejecución independientes, de manera que la configuración y librerías de uno no entren en conflicto con los de otro.**

Un entorno virtual está compuesto por **un intérprete de Python, una configuración específica y ibrerías independientes.**

## Instalación de virtualenv

Para instalar virtualenv nos ayudaremos de otra herramienta que viene instalada junto con el intérprete de Python: <code>pip</code>. Pip es una utilidad de línea de comandos que nos permite instalar y administrar librerías y paquetes Python. Muchos de estos paquetes y librerías se encuentran alojados en el <a hrer="https://pypi.org">Python Package Index</a> o PyPI, el repositorio oficial para paquetes de terceros.

El comando para instalar virtualenv con pip es el siguiente:

```
$ pip install virtualenv
```

