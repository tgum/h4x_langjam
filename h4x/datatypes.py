from pprint import pprint
import json
from . import runner

class BasicType:
	def __init__(self):
		self.type = "NULL"
	def __repr__(self):
		return self.type
class Value(BasicType):
	def __init__(self):
		self.type = "VALUE"
	def __repr__(self):
		return self.type + ":" + str(self.value)
class Null(Value):
	def __init__(self):
		self.type = "NULL"
		self.value = None
class Number(Value):
	def __init__(self, value):
		self.type = "NUMBER"
		self.value = int(value)
class String(Value):
	def __init__(self, value):
		self.type = "STRING"
		self.value = value
class Bool(Value):
	def __init__(self, value):
		self.type = "BOOLEAN"
		self.value = value

class Exec(BasicType):
	def __init__(self):
		self.type = "EXEC"

class EvaledExec(Exec):
	def __init__(self):
		self.type = "EVALED_EXEC"
class PyExec(EvaledExec):
	def __init__(self, function, num_args):
		self.type = "PY_EXEC"
		self.exec = function
		self.num_args = num_args
class H4xExec(EvaledExec):
	def __init__(self, arg_names, function):
		self.type = "H4X_EXEC"
		self.arg_names = arg_names
		self.num_args = len(arg_names)
		self.func_body = function
	def exec(self, args, scopes):
		scopes.append({})
		for i, arg in enumerate(args):
			scopes[-1][self.arg_names[i]] = arg
		result = runner.eval(self.func_body, scopes)
		scopes.pop()
		return result

class SpecialExec(Exec):
	def __init__(self, function):
		self.type = "SPECIAL_EXEC"
		self.exec = function