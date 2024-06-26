from pprint import pprint

import h4x

exports = {}

# //---CONDITIONAL---\\ #
def func_if(args, scopes):
	if len(args) >= 2:
		condition = h4x.eval(args[0], scopes)
		if isinstance(condition, h4x.datatypes.Bool):
			if condition.value:
				body_true = args[1]
				result = h4x.eval(body_true, scopes)
				return result
			elif len(args) > 2:
				body_false = args[2]
				result = h4x.eval(body_false, scopes)
				return result
			else:
				return h4x.datatypes.Null()
		else:
			raise Exception("the first argument to if must be a boolean")
	else:
		raise Exception("if needs at least 2 arguments")


# //---LOOPS---\\ #
def func_repeat(args, scopes):
	scopes.append({})
	result = h4x.datatypes.Null()
	amount = h4x.eval(args[0], scopes).value
	for i in range(amount):
		result = h4x.eval(args[1:], scopes)
	scopes.pop()
	return result

def func_while(args, scopes):
	scopes.append({})
	result = h4x.datatypes.Null()
	body = args[1:]
	while True:
		condition = h4x.eval(args[0], scopes)
		if not condition.value:
			break
		result = h4x.eval(body, scopes)
	scopes.pop()
	return result


exports["if"] =     h4x.datatypes.SpecialExec(func_if)
exports["repeat"] = h4x.datatypes.SpecialExec(func_repeat)
exports["while"] =  h4x.datatypes.SpecialExec(func_while)