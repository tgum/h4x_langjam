import datatypes
import tokens

exports = {}
def func_print(args, scopes):
	print(args[0].value)
	return args[0]
def func_add(args, scopes):
	return datatypes.Number(args[0].value + args[1].value)
def func_sub(args, scopes):
	return datatypes.Number(args[0].value - args[1].value)

def func_define(args, scopes, eval):
	varname = args[0].data
	value = eval(args[1])

	scopes[0][varname] = value
	return value

exports["define"] = datatypes.SpecialExec(func_define)

exports["print"] = datatypes.PyFunc(func_print, 1)
exports["+"] = datatypes.PyFunc(func_add, 2)
exports["-"] = datatypes.PyFunc(func_sub, 2)