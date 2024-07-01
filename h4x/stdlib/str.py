import h4x

def func_upper(args, scopes):
	return h4x.datatypes.String(args[0].value.upper())
def func_lower(args, scopes):
	return h4x.datatypes.String(args[0].value.lower())

exports = {}
exports["str:upper"] = h4x.datatypes.PyExec(func_upper, 1)
exports["str:lower"] = h4x.datatypes.PyExec(func_lower, 1)
