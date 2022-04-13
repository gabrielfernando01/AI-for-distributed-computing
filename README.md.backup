![](https://raw.githubusercontent.com/gabrielfernando01/numpy/master/image/conditional.png)


# Conditional Statements in Python

Frequenly, a program needs to skip over some statements, executea series of statements repetitively, or choose between alternate sets of statements to execute.

That is where **control structures** come in. A control structure directs the order of execution of the statements in a program(referred to as the program's flow).

## Introduction to the if Statement

We'll start by looking at the most basic type of if statement. In its simplest form, it look like this:

```
if <expr>:
	<statement>
```

In the form shown above:

- 'expr' is an expression evaluated in a Boolean context.
- 'statement' is a valid Python statement, which must be indented.

Note that the colon(:) following 'expr' is required.

## Grouping Statements: Indetation and Blocks

The usual approach taken by most programming languages is to define a syntactic  device that groups multiple statements into one **compound statement** or **block.** A block is regarded syntactically as a single entity. When it is the target of an if statement, and 'expr' is true, then all the statements in the block are executed. If 'expr' is false, then none of them are.

### Python: It's All About the Indentation

![](https://raw.githubusercontent.com/gabrielfernando01/numpy/master/image/if.gif)

Python follows a convention known as the off side rule, a term coined by British computer scientist Peter J.Landin. (The term is taken from the offside law in association football.) Languages that adhere to the off side rule define blocks by identation. Python is one of a relatively small set of [off side rule languages](https://en.wikipedia.org/wiki/Off-side_rule#Off-side_rule_languages).

Consider the script file foo.py

```
if 'foo' in ['bar', 'baz', 'qux']:

	print('Expression was true')
	print('Executing statement in suite')
	print('...')
	print('Done')
print('After conditional')
```

Running foo.py produces this output:

***
IPython command prompt
***

```
[46]: %run foo.py
After conditional
```

Blocks can be nested to arbitrary depth. Each indent defines a new block, and each outdent ends the preceding block. The resulting structure is straightforward, consistent, and intuitive.

Here is a more complicated script file called block.py

```
# Does line execute?							Yes		No
#											---		---		
if 'foo' in ['foo', 'bar', 'baz']:			# x
	print('Outer condition is true')			# x
	
	if 10 > 20:								# x
		print('Inner conditioon 1')			#		 x
		
	print('Between inner conditions')			# x
	
	if 10 < 20:								# x
		print('Inner condition 2')			# x
		
	print('End of outer condition')			# x
print('After outer condition')				# x
```

The output generated when this script is run is shown below:

***
IPython Qtconsole
***

```
In [23]: %run block.py
Outer condition is true
Between inner conditions
Inner condition 2
After outer condition
```

## The else and elif Clauses

Now you know how to use an if statement to conditionally execute a single statement or a block of several statements. It's time to find out what else you can do.

Sometimes, you want to evaluate a condition and take one path if it is true but specify an alternative path it is not. This is accomplished with an else clause:

```
if <expr>:
	<statement(s)>
else:
	<statemet(s)>
```

If 'expr' is true, the first suite is executed, and the second is skipped. If 'expr' is false, the first suite is skipped and the second is executed. Either way, execution then resumes after the second suite. Both suites are defined by indentetion, as described above.

In this example, x is less than 50, so the first suite (the first two prints) are excecuted, and the second suite (two last prints) are skipped:

```
x = 20

if x < 50:
	print('(first suite)')
	print('x is small')
else:
	print('(second suite)')
	print('x is large')
```

Here, on the other hand, x is greater than 50, so the first suite is passed over, and the second suite executed:

```
x = 120

if x < 50
	print('(first suite)')
	print('x is small')
else:
	print('(second suite)')
	print('x is large')
```

