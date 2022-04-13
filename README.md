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

![](https://raw.githubusercontent.com/gabrielfernando01/numpy/master/image/if.gif)

Running foo.py produces this output:

***
IPython command prompt
***

```
[46]: %run foo.py
After conditional
```

