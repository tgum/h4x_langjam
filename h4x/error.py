import h4x
import sys

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

def token_error(message, index):
	line_num, line_index = get_line(index, h4x.program)
	line = h4x.program.split('\n')[line_num]
	print(f"There has been an error during parsing")
	print(f"at line {line_num+1} character {index - line_index}")
	print(f"{line}")
	print(f"{'^'.rjust(index - line_index)}")
	print(message)
	sys.exit()
	raise Exception(message)

def runtime_error(message):
	raise Exception(message)