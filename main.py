from pprint import pprint

import lexer
import parser
import runner

with open("test.h4x", "r") as f:
	program = f.read()
lexed = lexer.tokenize(program)
parsed = parser.parse(lexed)
evaled = runner.eval(parsed)
#print(program)
#print(lexed)
#pprint(parsed)
print(evaled)