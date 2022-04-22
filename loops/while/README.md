![](https://raw.githubusercontent.com/gabrielfernando01/numpy/master/image/while.png)

## Python 'while' Loops (Indefinite Iteration)

**Iteration** means executing the same block of code over and over, potentially many times. A programming structute that implements iteration is called a **loop.**

In programming, there are two types of iteration, indefinite and definite:

- With **indefinite iteration**, the number of times the loops is executed isn't specified explicity in advance. Rather, the designated block is executed repeatedly as long as some condition is meat

- With **definite iteration,** the number of times the designated block will be executed is specified explicity at the time the loop start.

### The while Loop

The format of a rudimentary while loop is shown below:

```
while <expr>:
  <statement(s)>
```

<statment(s)> represents the block to be repeatedly executed , often referred to as the body of the loop. This is denoted with identation, just as in a if statement.

The controlling expression. 'expr', typically involves one or more variables that are initializad prior to starting the loop and the modified somewhere in the loop body.

When a while loop es encountered, 'expr' is first evaluated in Boolean context. If it is true, the loop body is executed. The 'expr' is checked again, and if still true, the body is executed aagain. This continues until 'expr' becomes false, at which point program execution proceeds to the first statement beyond the loop body.

```
n = 5
while n > 0:
  n -= 1
  print(n)
```

![](https://raw.githubusercontent.com/gabrielfernando01/numpy/master/image/while.gif)

Note that the controlling expression of the while loop es tested first, before anything else happens. If's false to start with, the loop boody will never be excecuted at all: 

```
n = 0
while n > 0:
  n -= 1
  print(n)
```

Here's another while loop involving a list, rather than a numeric comparison:

```
a = ['foo', 'bar', 'baz']
while a:
  print(a.pop(-1))
```

When a list is evaluated in Boolean context, it is truthy if it has elements in it and falsy if it is empty. In this example, **a** is true as long as it has elements in it. Once all the items have been removed with the .pop() method and the list is empty, **a** is false, and the loop terminates.

### The Python break and continue Statements

Python provides two keywords that termite a loop iteration prematurale:

- The Python **break** statement immediately terminates a loop entirely. Program excecution porceeds to the first statement following the loop body.
- The Python **continue** statement immediately terminates the current loop iteration. Execution jumps to the top of the loop, and the controlling expression is re-evaluated to determine whether the loop will excecute again or terminate.
  
The distinction between break and continue is demonstrated in the following diagram: 

![](https://raw.githubusercontent.com/gabrielfernando01/numpy/master/image/diagram.png)

Here's script file called break.py that demostrates the break statement:

```
n = 5
while n > 0:
  n -= 1
  if n == 2:
    break
  print(n)
print('Loop ended.')
```

When 'n' becomes '2', the break statement is executed. The loop is terminated completely, and program execution jumps to the print() statement on line 7.

The next script, continue.py, is identical except for a continue statement in place of the break:

```
n = 5
while n > 0
  n -= 1
  if n == 2
    continue
  print(n)
print('Loop ended.'
```
### The else Clause

Python allows an optional else clause at the end of a while loop. This is a unique feature of Python, not found in mosth other programming languages. The syntax is show below:

```
while <expr>
  <statement(s)>
 else:
  <additinal_statement(s)>
```

The 'additional_statement(s)' specified in the else clause will be executed when the while loop terminates.

About now, you may be thinking, "How  is that useful?" You could accomplish the same thing by purring those statements immediately after the while loop, whithout the else:

```
while <expr>:
  <statement(s)>
<additional_statement(s)>
```

In the latter case, whithout the else clause, 'additional_statement(s)' wil be excuted after the while loop terminates, no matter what.

When 'additional_statement(s)' are placed in an else clause, they will be executed only if the loop terminates "by exhaustion" -that is, if the lop iterates until the controlling condition become false. If the loop is exited by a break statement, the else clause won't be executed.

Consider the following example:

```
n = 5
while n > 0:
  n -= 1
  print(n)
else:
  print('Loop done.')
```
In this case, the loop repeated until the condition was exhausted: 'n' became 0, so n > 0 became false. Becase the loop lived out its natural life, so to speak, the else clause was executed. Now observe the difference here:

```
n = 5
while n > 0:
  n -= 1
  print(n)
  if n == 2:
    break
 else:
 print('Load done.')
```

The loop is terminated prematurely with break, so the else clause isn't executed.

When might an else clause on a while loop be useful? One common situation is if you are searching a list for a specific item. You can use break to exit the loop if the item is found, and the else clause can contain code that is meant to be executed if the item isn't found:

```
a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'

i = 0
while i < len(a):
  if a[i] == s:
    # Processing fot item found
    break
  i += 1
else:
  #Processing for item not found
  print(s, 'not found in list.')
```

***
**Note:** The code show above is useful to illustrate the concept, but you'd actually be very unlikely to search a list that way.

First of all, lists are usually processed with definite iteration, not a while loop. Definite iteration is covered in the next tutorial in this series.

Secondly, Python porvides built-in ways to search for an item in a list. You can use the **in** operator:

```
if s in a:
  print(s, 'found in list.')
else:
  print(s, 'not found in list.')
```

The list.index() method would also work. This method raises a ValueError axception if the item isn't found in the list, so you need to understand exception handling to use it. In Python, you use a try statement to handle an exception. An example is given below:

```
try:
  print(a.index('courge'))
except ValueError:
  print(s, 'not found in list.')
```
***

An else clause with while loop is a bit of an oddity, not often seen. But don't shy away from it if you find a situation in which you feel it adds clarity to your code!.

### Infinite Loops

Suppose you write a while loop that theoretically never ends. Sounds weird, right?

Consider this example:

```
while True:
  print('foo')
```

Maybe that doesn't sound like something you'd want to do, but this pattern is actually quite common. For example, you might write code for a service that starts up and runs forever accepting service requests. "Forever" in this context means until yoou shut it down, or until the heat death of the universe, whichever comes first.

Here's another variant of the loop shown above that successively removes items from a lis using .pop() until is empty:

```
a = ['foo', 'bar', 'baz']
while True:
  if not a:
    break
  print(a.pop(-1))
```

When 'a' becomes empty, not 'a' becomes true, and the break statement exits the loop.

You can also specify multiple break statements in a loop:

```
while True:
  if <expr1>: # One condition for loop termination
    break
  ...
  if <expr2>: # Another termination condition
    break
  ...
  if <expr3>: # Yet another
    break
```

In this case like this, where there are multiple reason to end the loop, it is often cleaner to break out from several different locations, rather than try to specify all the termination conditions in the loop header.

Infinite loops can be vary useful. Just remember that you must ensure the loop gets broken out of at some point, so it doesn't truly become infinite.

## One-Line while Loops

As with an if statement, a while loop can be specified on one line. If there are multiple statements in the block that makes up the loop body, they can be separated by semicolons(;):

```
n > 5
while n > 0: n -= 1 ; print(n)
```

This only works whith simple statements though. You can't combine two compound statements into one line. Thus, you can specify a while loop all on one line as above, and you write an if statement on one line:

```
if True: print('foo')
```

But you can't do this:

```
>>> while n > 0: n -=1; if True: print('foo')
SyntaxisError: invalid syntax 
```

Remember that PEP 8 discourages multiple statemnets on one line. So you probably shouldn't be doing any of this very often anyhow.

## Coclusion

In this tutorial, you learned about **indefinite iteration** using the Python while loop. You're now able to:

- Construct basic and complex while loops
- Interrupt loop execution whith break and continue
- Use the else clause with a while loop
- Deal with infinite loops

