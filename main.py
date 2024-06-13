import lexer
import parser
from pprint import pprint

with open("test.h4x", "r") as f:
	program = f.read()
lexed = lexer.tokenize(program)
parsed = parser.parse(lexed)
#print(program)
#print(lexed)
pprint(parsed)