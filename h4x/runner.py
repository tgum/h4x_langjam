import pprint

from . import datatypes
from . import tokens


DEBUG = False


def prettyprint(stuff):
	pretty = pprint.pformat(stuff)
	for line in pretty.split("\n"):
		print("   " * depth + line)

depth = -1

def eval(expr, scopes):
	global depth
	depth += 1
	if DEBUG:
		print()
		prettyprint("evaling")
		prettyprint(expr)

	evaled = None
	if type(expr) == list:
		evaled = []
		if len(expr) > 0:
			first = eval(expr[0], scopes)
			evaled = [first]
			if isinstance(first, datatypes.Exec):
				if isinstance(first, datatypes.SpecialExec):
					evaled = first.exec(expr[1:], scopes)
				elif isinstance(first, datatypes.EvaledExec):
					for subexpr in expr[1:]:
						evaled.append( eval(subexpr, scopes) )
					
					if len(evaled) - 1 == first.num_args:
						evaled = first.exec(evaled[1:], scopes)
					else:
						raise Exception(f"{first} expected {first.num_args} but got {len(evaled) - 1}")
			else:
				for subexpr in expr[1:]:
					if isinstance(subexpr, datatypes.BasicType):
						evaled.append(subexpr)
					else:
						evaled.append( eval(subexpr, scopes) )
				if len(evaled) > 0:
					evaled = evaled[-1]
				
	elif expr.type == tokens.TokenTypes.STRING:
		evaled = datatypes.String(expr.data)

	elif expr.type == tokens.TokenTypes.NUMBER:
		evaled = datatypes.Number(expr.data)

	elif expr.type == tokens.TokenTypes.IDENTIFIER:
		for scope in reversed(scopes):
			if expr.data in scope:
				evaled = scope[expr.data]
				break
		if evaled == None:
			raise Exception(f"{expr.data} is not defined in any scope")
	elif isinstance(expr, datatypes.BasicType):
		return expr

	if DEBUG:
		prettyprint("returns")
		prettyprint(evaled)
		input("")

	depth -= 1
	return evaled

