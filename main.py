import lexer

with open("test.h4x", "r") as f:
	program = f.read()
lexed = lexer.lex(program)
print(program)
print(lexed)