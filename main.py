from pprint import pprint

import h4x

scope_stack = []
scope_stack.append({})

h4x.import_module(scope_stack[0], "h4x.stdlib")

with open("test.h4x", "r") as f:
	program = f.read()
	
lexed = h4x.tokenize(program)
parsed = h4x.parse(lexed)
evaled = h4x.eval(parsed, scope_stack)
print(evaled)