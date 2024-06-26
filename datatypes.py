class BasicType:
	def __init__(self):
		self.type = "NULL"
class Number(BasicType):
	def __init__(self, value):
		self.type = "NUMBER"
		self.value = int(value)
class String(BasicType):
	def __init__(self, value):
		self.type = "STRING"
		self.value = value

class Exec(BasicType):
	def __init__(self):
		self.type = "CALLABLE"
		self.exec = print
		self.num_args = 1
class PyFunc(Exec):
	def __init__(self, function, num_args):
		self.type = "PY_FUNC"
		self.exec = function
		self.num_args = num_args

class SpecialExec(BasicType):
	def __init__(self, function):
		self.type = "SPECIAL_EXEC"
		self.exec = function