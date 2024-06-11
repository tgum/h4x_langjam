import lexer

with open("test.h4x", "r") as f:
	program = f.read()
lexed = lexer.tokenize(program)
print(program)
print(lexed)