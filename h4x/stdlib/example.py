import h4x

exports = {}
def func_zoob(args, scopes):
	print("tosty")
	return h4x.datatypes.String("tosty")

exports["example:tosty"] = h4x.datatypes.PyExec(func_zoob, 0)
