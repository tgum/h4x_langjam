from pprint import pprint

import h4x

exports = {}
def func_list(args, scopes):
	print("makelist")
	return h4x.datatypes.String("makelist")

exports["#l"] = h4x.datatypes.SpecialExec(func_list)