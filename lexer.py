from collections import namedtuple
from pprint import pprint
from enum import Enum
import string

tokens = []
index = 0
program = ""

Token = namedtuple("Token", "type data")

def currchar():
	return program[index]

def nextchar(amt=1):
	global index
	index = index + amt
	return index

def make_token():
	global build_type, currently_building, tokens
	tokens.append(Token(build_type, currently_building))
	build_type = TokenTypes.UNDEFINED
	currently_building = ""

class TokenTypes(Enum):
	UNDEFINED = 0
	NUMBER = 1
	STRING = 2
	IDENTIFIER = 3
	OPEN_PAREN = 4
	CLOSE_PAREN = 5

currently_building = ""
build_type = TokenTypes.UNDEFINED


"""
token types:
( OPEN PAREN
) CLOSE PAREN
012.41 NUMBER
"qsdfj" STRING
hello_10 IDENTIFIER
"""

def tokenize(prog):
	global program, index, tokens, build_type, currently_building
	program = prog
	
	currently_building = ""
	build_type = TokenTypes.UNDEFINED
	tokens = []
	index = 0

	while index < len(program):
		char = currchar()
		if build_type == TokenTypes.UNDEFINED:
			if char == "(":
				currently_building += char
				build_type = TokenTypes.OPEN_PAREN
				make_token()
			elif char == ")":
				currently_building += char
				build_type = TokenTypes.CLOSE_PAREN
				make_token()
			elif char == "\"":
				build_type = TokenTypes.STRING
			elif char in string.digits:
				currently_building += char
				build_type = TokenTypes.NUMBER
			elif char == " ":
				pass
			else:
				currently_building += char
				build_type = TokenTypes.IDENTIFIER
		elif build_type == TokenTypes.STRING:
			if char == "\"" and program[index-1] != "\\":
				make_token()
			else:
				currently_building += char
		elif build_type == TokenTypes.NUMBER:
			if char in string.digits or char == ".":
				currently_building += char
			elif True:
				make_token()
				nextchar(-1)
			else:
				currently_building += char
				raise Exception(f"t3re 1s s0m371n9 b4d w17h ur numb3r. {currently_building} h4s {char}. n0t g00d")
		elif build_type == TokenTypes.IDENTIFIER:
			if char == " ":
				make_token()
			elif char == ")":
				make_token()
				nextchar(-1)
			else:
				currently_building += char

		nextchar()
	if build_type != TokenTypes.UNDEFINED:
		raise Exception(f"unf1n1s3d token. {currently_building} should be a {build_type} but it wasnt finished")
	return tokens