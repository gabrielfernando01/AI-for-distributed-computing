# ==========================================================================
# NumPy Tutorial: You First Steps Into Data Sciene in Python.
# Python 'while' loops

#Considere this loop:
n = 5
while n > 0:
    print -= 1
    print(n)

# If's false to start with, the loop boody will never be excecuted at all: 
n = 0
while n > 0:
  n -= 1
  print(n)
  
# Here's another while loop involving a list, rather than a numeric comparison:
a = ['foo', 'bar', 'baz']
while a:
  print(a.pop(-1))
  
# Here's script file called break.py that demostrates the break statement:
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')

# The next script, continue.py, is identical except for a continue statement in place of break:
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

# The else clause
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

# Now observe the difference here:
n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')

# If you are searching a list for a specific item
a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'

i = 0
while i < len(a):
    if a[i] == s
        # Processing for item found
        break
    i += 1
    else:
        # Processing for item not found
        print(s, 'not found in list')

# Here's another variant of the loop shown above that succesively removes items from a list using .pop() until it is empty.
a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop(-1))

