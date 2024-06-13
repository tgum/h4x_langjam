import lexer
from pprint import pprint

parsed = []

def parse(tokens, depth=0):
	tree = []
	i = 0
	while i < len(tokens):
		token = tokens[i]
		value = token
		if token.type == lexer.TokenTypes.OPEN_PAREN:
			match_index = get_matching(i, tokens)
			value = parse(tokens[i+1 : match_index], depth+1)
			i = match_index
		tree.append(value)
		i += 1
	return tree

def get_matching(start, tokens):
	depth = 0
	index = start
	while depth >= 0:
		index += 1
		token = tokens[index]
		if token.type == lexer.TokenTypes.OPEN_PAREN:
			depth += 1
		elif token.type == lexer.TokenTypes.CLOSE_PAREN:
			depth -= 1
	return index