from pprint import pprint

import h4x

exports = {}
def func_list(args, scopes):
	evaled = []
	for arg in args:
		evaled.append(h4x.eval(arg, scopes))
	return h4x.datatypes.H4xList(evaled)

def func_len(args, scopes):
	if not isinstance(args[0], h4x.datatypes.H4xList):
		h4x.error.runtime(f"The first argument to #len needs to be a H4xList, instead it got {repr(args[0])}")
	return h4x.datatypes.Number(args[0].len())
def func_index(args, scopes):
	if not isinstance(args[0], h4x.datatypes.H4xList):
		h4x.error.runtime(f"The first argument to #nth needs to be a H4xList, instead it got {repr(args[0])}")
	if not isinstance(args[1], h4x.datatypes.Number):
		h4x.error.runtime(f"The second argument to #nth needs to be a number, instead it got {repr(args[1])}")
	return args[0].index(args[1].value)
def func_push(args, scopes):
	if not isinstance(args[0], h4x.datatypes.H4xList):
		h4x.error.runtime(f"The first argument to #push needs to be a H4xList, instead it got {repr(args[0])}")
	return args[0].push(args[1])
def func_pop(args, scopes):
	if not isinstance(args[0], h4x.datatypes.H4xList):
		h4x.error.runtime(f"The first argument to #push needs to be a H4xList, instead it got {repr(args[0])}")
	return args[0].pop()
def func_set(args, scopes):
	if not isinstance(args[0], h4x.datatypes.H4xList):
		h4x.error.runtime(f"The first argument to #set needs to be a H4xList, instead it got {repr(args[0])}")
	if not isinstance(args[1], h4x.datatypes.Number):
		h4x.error.runtime(f"The second argument to #set needs to be a number, instead it got {repr(args[1])}")
	return args[0].set(args[1].value, args[2])

exports["#l"] = h4x.datatypes.SpecialExec(func_list)

exports["#len"] = h4x.datatypes.PyExec(func_len, 1)
exports["#nth"] = h4x.datatypes.PyExec(func_index, 2)
exports["#push"] = h4x.datatypes.PyExec(func_push, 2)
exports["#pop"] = h4x.datatypes.PyExec(func_pop, 1)
exports["#set"] = h4x.datatypes.PyExec(func_set, 3)