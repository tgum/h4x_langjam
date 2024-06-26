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
class Bool(Value):
	def __init__(self, value):
		self.type = "BOOLEAN"
		self.value = value

class H4xList(Value):
	def __init__(self, value):
		self.type = "LIST"
		self.value = value

	def len(self):
		return len(self.value)
	def index(self, i):
		return self.value[i]
	def push(self, value):
		result = self.value[:]
		result.append(value)
		return H4xList(result)
class String(H4xList):
	def __init__(self, value):
		self.type = "STRING"
		self.value = value

	def index(self, i):
		return String(self.value[i])
	def push(self, value):
		result = self.value + str(value.value) # TEMPORARY STRINGIFICATION
		return String(result)

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