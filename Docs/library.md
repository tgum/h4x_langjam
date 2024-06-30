# Embedding h4x in your own projects

First you need to put the h4x folder in your project folder.
idk how to install it system wide maybe ill upload it to pip someday

After that you need to import h4x
```python
import h4x
```

Then you need to create scopes, thats a just list of dictionaries with all the variables.
```python
scopes = h4x.create_scopes()
```

Import the standard library with the basic functions (`if`, `+`, `define`).
If you want you can use your own if you want to limit access to certain functions.
the h4x.import_module function takes a scope (dictionary) and imports the second argument into it.
```python
h4x.import_module(scopes[0], "h4x.stdlib")
```

Then you parse whatever program you want to run. (technically it does the tokenizing and the parsing see [parsing](#parsing))
```python
parsed_program = h4x.parse(program)
```

After you can just evaluate that tree
```python
h4x.eval(parsed_program, scopes)
```

# Notes

## parsing

If you want more control you can call the `h4x.tokenize` on your program, then call `h4x.tokens_to_tree` on the tokens returned by tokenize.
Also you can validate a token list by calling `h4x.parse.is_valid_program(tokens)`

## modules/importing

Modules are just python files with an `exports` dictionary which will be merged with the top scope.
Each key is the name of the variable and its value is an instance of the classes in `h4x.datatypes`. 


### creating a module tutorial
Let's make a module called `foo` with a function `foo:bar` which prints baz.
Create a file "foo.py" and put it in the same folder as the file that runs h4x.eval
```python
import h4x

exports = {}
def func_bar(args, scopes):
	print("baz")
	return h4x.datatypes.String("baz")

exports["foo:bar"] = h4x.datatypes.PyExec(func_bar, 0)
```
So first you import h4x to get access to the datatypes and stuff.
Then you create and exports variable which is 