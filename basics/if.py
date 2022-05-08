# Python if - Sentencia if de control de flujo
# La sentencia if se utiliza para ejecutar un bloque de código si, y solo si, 
# se cumple una determinada condición. 
if condicion:
    bloque de codigo

x = 17
if x < 20:
    print('x es menor que 20')

values = [1, 2, 3, 4, 5]
if 5 in values:
    print('5 is in values')
print('End')

# Sententencia if ... else.
if condicion:
    bloque de codigo    # Cuando condición se evalúa a True
else:
    bloque de código    # Cuando condición se evalúa a False

# Si divides un número entre 0, el programa lanzará un error y terminará. Para
# evitar esto, podemos añadir la sentencia if ... else.
result = None
x = 10
y = 2
if y != 0:
    result = x / y
else:
    result = f'(y) no tiene inverso multiplicativo.'
print(result)

# if ... elif ... else
if cond1:
    bloque cond1    # Sentencia que se evalúa si la cond1 es True
elif cond2:
    bloque cond2    # Sentencia que se evalúa si la cond1 es False pero cond2 es True
...
else:
    bloque else     # Sentencia si todas las condiciones se evalúan a False

# Si queremos comprobar si un número es menor que 0, igual a 0, o mayor que 0 y en
# cada situación debemos ejecutar un código diferente.
x = 28
if x < 0:
    print(f'{x} es menor que 0')
elif x > 0:
    print(f'{x} es mayor que 0')
else:
    print(f'x es 0')

# Sentencias if anidadas
x = 28
if x < 0:
    print(f'{x} es menor que 0')
else:
    if x > 0:
        print(f'{x} es mayor que 0')
    else:
        print('x es cero')







