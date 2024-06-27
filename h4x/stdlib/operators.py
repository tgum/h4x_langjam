from pprint import pprint

import h4x

exports = {}

def func_float(args, scopes):
	return h4x.datatypes.Float(args[0].value)
def func_int(args, scopes):
	return h4x.datatypes.Number(args[0].value)

# //---BASIC MATH---\\ #
def func_add(args, scopes):
	return h4x.datatypes.Float(args[0].value + args[1].value)
def func_sub(args, scopes):
	return h4x.datatypes.Float(args[0].value - args[1].value)
def func_mul(args, scopes):
	return h4x.datatypes.Float(args[0].value * args[1].value)
def func_div(args, scopes):
	return h4x.datatypes.Float(args[0].value / args[1].value)


# //---COMARITION---\\ #
def func_eq(args, scopes):
	return h4x.datatypes.Bool(args[0].value == args[1].value)
def func_neq(args, scopes):
	return h4x.datatypes.Bool(args[0].value != args[1].value)
def func_lt(args, scopes):
	return h4x.datatypes.Bool(args[0].value < args[1].value)
def func_gt(args, scopes):
	return h4x.datatypes.Bool(args[0].value > args[1].value)
def func_lt_eq(args, scopes):
	return h4x.datatypes.Bool(args[0].value <= args[1].value)
def func_gt_eq(args, scopes):
	return h4x.datatypes.Bool(args[0].value >= args[1].value)

# //---BOOLEAN---\\ #
def func_not(args, scopes):
	return h4x.datatypes.Bool(not args[0].value)
def func_and(args, scopes):
	return h4x.datatypes.Bool(args[0].value and args[1].value)
def func_or(args, scopes):
	return h4x.datatypes.Bool(args[0].value or args[1].value)


exports["int"] =   h4x.datatypes.PyExec(func_int, 1)
exports["float"] = h4x.datatypes.PyExec(func_float, 1)

exports["+"] =   h4x.datatypes.PyExec(func_add, 2)
exports["-"] =   h4x.datatypes.PyExec(func_sub, 2)
exports["*"] =   h4x.datatypes.PyExec(func_mul, 2)
exports["/"] =   h4x.datatypes.PyExec(func_div, 2)

exports["=="] =  h4x.datatypes.PyExec(func_eq, 2)
exports["!="] =  h4x.datatypes.PyExec(func_neq, 2)
exports["<"] =   h4x.datatypes.PyExec(func_lt, 2)
exports[">"] =   h4x.datatypes.PyExec(func_gt, 2)
exports["<="] =  h4x.datatypes.PyExec(func_lt_eq, 2)
exports[">="] =  h4x.datatypes.PyExec(func_gt_eq, 2)

exports["not"] = h4x.datatypes.PyExec(func_not, 1)
exports["and"] = h4x.datatypes.PyExec(func_and, 2)
exports["or"] =  h4x.datatypes.PyExec(func_or, 2)