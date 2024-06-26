from pprint import pprint
import string

from . import tokens

tokens_list = []
index = 0
program = ""


def currchar():
	return program[index]

def nextchar(amt=1):
	global index
	index = index + amt
	return index

def make_token():
	global build_type, currently_building, tokens_list
	tokens_list.append(tokens.Token(build_type, currently_building))
	build_type = tokens.TokenTypes.UNDEFINED
	currently_building = ""


currently_building = ""
build_type = tokens.TokenTypes.UNDEFINED


"""
token types:
( OPEN PAREN
) CLOSE PAREN
012.41 NUMBER
"qsdfj" STRING
hello_10 IDENTIFIER

~ hello this is comment COMMENT
{hello this is comment} MULTILINE_COMMENT
"""

def tokenize(prog):
	global program, index, tokens_list, build_type, currently_building
	program = prog
	
	currently_building = ""
	build_type = tokens.TokenTypes.UNDEFINED
	tokens_list = []
	index = 0

	while index < len(program):
		char = currchar()
		if build_type == tokens.TokenTypes.UNDEFINED:
			if char == "(":
				currently_building += char
				build_type = tokens.TokenTypes.OPEN_PAREN
				make_token()
			elif char == ")":
				currently_building += char
				build_type = tokens.TokenTypes.CLOSE_PAREN
				make_token()
			elif char == "\"":
				build_type = tokens.TokenTypes.STRING
			elif char in string.digits:
				currently_building += char
				build_type = tokens.TokenTypes.NUMBER
			elif char in string.whitespace:
				pass
			elif char == "~":
				build_type = tokens.TokenTypes.COMMENT
			elif char == "{":
				build_type = tokens.TokenTypes.MULTILINE_COMMENT
			else:
				currently_building += char
				build_type = tokens.TokenTypes.IDENTIFIER
		elif build_type == tokens.TokenTypes.STRING:
			if char == "\"" and program[index-1] != "\\":
				make_token()
			else:
				currently_building += char
		elif build_type == tokens.TokenTypes.NUMBER:
			if char in string.digits or char == ".":
				currently_building += char
			elif True:
				make_token()
				nextchar(-1)
			else:
				currently_building += char
				raise Exception(f"t3re 1s s0m371n9 b4d w17h ur numb3r. {currently_building} h4s {char}. n0t g00d")
		elif build_type == tokens.TokenTypes.IDENTIFIER:
			if char in [" ", "\n"]:
				make_token()
			elif char == ")":
				make_token()
				nextchar(-1)
			else:
				currently_building += char
		elif build_type == tokens.TokenTypes.COMMENT:
			if char == "\n":
				build_type = tokens.TokenTypes.UNDEFINED
				currently_building = ""
		elif build_type == tokens.TokenTypes.MULTILINE_COMMENT:
			if char == "}":
				build_type = tokens.TokenTypes.UNDEFINED
				currently_building = ""

		nextchar()
	if build_type != tokens.TokenTypes.UNDEFINED:
		raise Exception(f"unf1n1s3d token. {currently_building} should be a {build_type} but it wasnt finished")
	return tokens_list