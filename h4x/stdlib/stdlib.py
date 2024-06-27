from pprint import pprint

import h4x

exports = {}

# //---BASIC STUFFS IG?---\\ #
def func_print(args, scopes):
	print(args[0].value)
	return args[0]
def func_prnt_scope(args, scopes):
	pprint(scopes)

def func_do(args, scopes):
	scopes.append({})
	result = h4x.eval(args, scopes)
	scopes.pop()
	return result
def func_import(args, scopes):
	h4x.import_module(scopes[-1], args[0].data, args[0].data + ":")
	return h4x.datatypes.String(args[0].data)
def func_fn(args, scopes):
	arg_names = []
	for name in args[0]:
		arg_names.append(name.data)
	body = args[1:]
	return h4x.datatypes.H4xExec(arg_names, body)


def func_define(args, scopes):
	if len(args) != 2:
		raise Exception(f"Define needs two arguments: syntax (define a 5). It got {len(args)}")
	if args[0].type != h4x.tokens.TokenTypes.IDENTIFIER:
		raise Exception(f"the first parameter of define needs to be an identifier")
	varname = args[0].data
	value = h4x.eval(args[1], scopes)
	scopes[-1][varname] = value
	return value
def func_set(args, scopes):
	if len(args) != 2:
		raise Exception(f"set needs two arguments: syntax (set a 5). It got {len(args)}")
	if args[0].type != h4x.tokens.TokenTypes.IDENTIFIER:
		raise Exception(f"the first parameter of set needs to be an identifier")
	varname = args[0].data
	value = h4x.eval(args[1], scopes)
	for scope in reversed(scopes):
		if varname in scope:
			scope[varname] = value
			break
	return value


exports["do"] =     h4x.datatypes.SpecialExec(func_do)
exports["import"] = h4x.datatypes.SpecialExec(func_import)
exports["fn"] =     h4x.datatypes.SpecialExec(func_fn)

exports["define"] = h4x.datatypes.SpecialExec(func_define)
exports["set"] = h4x.datatypes.SpecialExec(func_set)

exports["print"] =  h4x.datatypes.PyExec(func_print, 1)
exports["scopes"] = h4x.datatypes.PyExec(func_prnt_scope, 0)

exports["true"] =  h4x.datatypes.Bool(True)
exports["false"] = h4x.datatypes.Bool(False)