import sys
import pprint

import h4x

h4x.DEBUG = False

scopes = h4x.create_scopes()
h4x.import_module(scopes[0], "h4x.stdlib")

def func_exit(args, scopes):
	print("Goodbye!")
	sys.exit()
def func_debug(args, scopes):
	h4x.DEBUG = not h4x.DEBUG
	if h4x.DEBUG:
		print("Debug mode activated")
	else:
		print("Debug mode disabled")

scopes[0]["exit"] = h4x.datatypes.PyExec(func_exit, 0)
scopes[0]["quit"] = scopes[0]["exit"]
scopes[0]["debug"] = h4x.datatypes.PyExec(func_debug, 0)

while True:
	program = input("> ") + "\n"
	tokenized = h4x.tokenize(program)
	while not h4x.parser.valid_program(tokenized):
		program += input(". ") + "\n"
		tokenized = h4x.tokenize(program)

	parsed = h4x.tokens_to_tree(tokenized)
	pprint(parsed)
	evaled = h4x.eval(parsed[0], scopes)
	print(evaled)


#(define plus5 (fn (a) (+ a 5) ) )