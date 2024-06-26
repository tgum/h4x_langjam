import importlib

import datatypes
import tokens

scope_stack = []
scope_stack.append({})
scope = scope_stack[0]

def import_module(module_name, prefix=""):
	module = importlib.import_module(module_name)
	for key in module.exports.keys():
		scope_stack[0][key] = module.exports[key]
default_modules = ["stdlib"]
for module_name in default_modules:
	import_module(module_name)

def eval(expr):
	evaled = None
	if type(expr) == list:
		function = eval(expr[0])
		if isinstance(function, datatypes.SpecialExec):
			evaled = function.exec(expr[1:], scope_stack, eval)
		else:
			evaled = []
			for i, subexpr in enumerate(expr):
				evaled.append(eval(subexpr))

			if isinstance(function, datatypes.Exec):
				if len(evaled)-1 == function.num_args:
					evaled = function.exec(evaled[1:], scope_stack)
				else:
					raise Exception(f"{function} expected {function.num_args} but got {len(evaled) - 1}")
			else:
				pass
				#print("not a function")
	elif expr.type == tokens.TokenTypes.IDENTIFIER:
		for i in range(len(scope_stack)-1, -1, -1):
			scope = scope_stack[i]
			if expr.data in scope:
				evaled = scope[expr.data]
				break
	elif expr.type == tokens.TokenTypes.STRING:
		evaled = datatypes.String(expr.data)
	elif expr.type == tokens.TokenTypes.NUMBER:
		evaled = datatypes.Number(expr.data)

	return evaled
