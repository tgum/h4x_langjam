from pprint import pprint

import h4x

exports = {}
def func_list(args, scopes):
	evaled = []
	for arg in args:
		evaled.append(h4x.eval(arg, scopes))
	return h4x.datatypes.H4xList(evaled)

def func_len(args, scopes):
	return h4x.datatypes.Number(args[0].len())
def func_index(args, scopes):
	return args[0].index(args[1].value)
def func_push(args, scopes):
	return args[0].push(args[1])

exports["#l"] = h4x.datatypes.SpecialExec(func_list)

exports["#len"] = h4x.datatypes.PyExec(func_len, 1)
exports["#nth"] = h4x.datatypes.PyExec(func_index, 2)
exports["#push"] = h4x.datatypes.PyExec(func_push, 2)