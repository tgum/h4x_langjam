from pprint import pprint

import h4x

exports = {}

# //---CONDITIONAL---\\ #
"""syntax
(if cond body_true optional_body_false)
"""
def func_if(args, scopes):
	if len(args) >= 2:
		condition = h4x.eval(args[0], scopes)
		if isinstance(condition, h4x.datatypes.Bool):
			if condition.value:
				scopes.append({})
				scopes[-1]["*trace"] = h4x.make_trace("if true")
				body_true = args[1]
				result = h4x.eval(body_true, scopes)
				scopes.pop()
				return result
			elif len(args) > 2:
				scopes.append({})
				scopes[-1]["*trace"] = h4x.make_trace("if true")
				body_false = args[2]
				result = h4x.eval(body_false, scopes)
				scopes.pop()
				return result
			else:
				return h4x.datatypes.Null()
		else:
			h4x.error.runtime("the first argument to if must be a boolean")
	else:
		h4x.error.runtime("if needs at least 2 arguments")


# //---LOOPS---\\ #
"""syntax
(repeat amount body)
"""
def func_repeat(args, scopes):
	if not len(args) >= 2:
		h4x.error.runtime(f"repeat needs at least 2 arguments, syntax: (repeat amount body), instead it got {len(args)}")
	scopes.append({})
	scopes[-1]["*trace"] = h4x.make_trace("repeat")
	result = h4x.datatypes.Null()
	amount = h4x.eval(args[0], scopes)
	if not isinstance(amount, h4x.datatypes.Number):
		h4x.error.runtime(f"The first argument to repeat must evaluate to a number, instead it evaluated to {repr(amount)}")
	for i in range(amount.value):
		result = h4x.eval(args[1:], scopes)
	scopes.pop()
	return result

"""syntax
(while cond body)
"""
def func_while(args, scopes):
	if not len(args) >= 2:
		h4x.error.runtime(f"while needs at least 2 arguments, syntax: (while cond body), instead it got {len(args)}")
	scopes.append({})
	scopes[-1]["*trace"] = h4x.make_trace("while")
	result = h4x.datatypes.Null()
	body = args[1:]
	while True:
		condition = h4x.eval(args[0], scopes)
		if not isinstance(condition, h4x.datatypes.Bool):
			h4x.error.runtime(f"The first argument to while must evaluate to a bool, instead it evaluated to {repr(condition)}")
		if not condition.value:
			break
		result = h4x.eval(body, scopes)
	scopes.pop()
	return result


exports["if"] =     h4x.datatypes.SpecialExec(func_if)
exports["repeat"] = h4x.datatypes.SpecialExec(func_repeat)
exports["while"] =  h4x.datatypes.SpecialExec(func_while)