import h4x
import sys

class H4xError(Exception):
	"""Any type of error that happened during running a h4x program"""

def get_line(index, string):
	line_num = 0
	line_index = 0
	for i, char in enumerate(string):
		if i == index:
			return line_num, line_index
		if char == "\n":
			line_index = i
			line_num += 1
	return line_num, line_index

def token(message, index):
	line_num, line_index = get_line(index, h4x.program)
	line = h4x.program.split('\n')[line_num]
	print(f"There has been an error during tokenization")
	print(message)
	print(f"at line {line_num+1} character {index - line_index}")
	print(f"{line}")
	print(f"{'^'.rjust(index - line_index)}")

	raise H4xError(message)
	sys.exit()

def parser(message, start):
	index = start.index
	line_num, line_index = get_line(index, h4x.program)
	line = h4x.program.split('\n')[line_num]

	print(f"There has been an error during parsing")
	print(f"{message}")
	print(f"at line {line_num+1} character {index - line_index}")
	print(f"{line}")
	print(f"{'^'.rjust(index - line_index)}")

	raise H4xError(message)
	sys.exit()

def runtime(message):
	index = h4x.DEBUG_last_token.index
	line_num, line_index = get_line(index, h4x.program)
	line = h4x.program.split('\n')[line_num]

	print(f"There has been an error during evaluation")
	print(f"{message}")
	print(f"at line {line_num+1} character {index - line_index}")
	print(f"{line}")
	print(f"{'^'.rjust(index - line_index)}")

	print("Traceback:")
	for scope in h4x.DEBUG_scopes:
		if "*trace" in scope:
			trace = scope["*trace"]
			line_num = 0
			if trace["token"] != None:
				token = trace["token"]
				line_num, line_index = get_line(token.index, h4x.program)

			line = h4x.program.split('\n')[line_num]
			print(f"  in {trace['scope']} at line {line_num+1}")
			print(f"  | {line}")
		else:
			print("no trace")

	raise H4xError(message)
	sys.exit()
