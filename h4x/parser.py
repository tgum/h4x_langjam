from . import tokens
from pprint import pprint

def parse(tokens_list, depth=0):
	tree = []
	i = 0
	while i < len(tokens_list):
		token = tokens_list[i]
		value = token
		if token.type == tokens.TokenTypes.OPEN_PAREN:
			match_index = get_matching(i, tokens_list)
			value = parse(tokens_list[i+1 : match_index], depth+1)
			i = match_index
		tree.append(value)
		i += 1
	return tree

def get_matching(start, tokens_list):
	depth = 0
	index = start
	while depth >= 0:
		index += 1
		token = tokens_list[index]
		if token.type == tokens.TokenTypes.OPEN_PAREN:
			depth += 1
		elif token.type == tokens.TokenTypes.CLOSE_PAREN:
			depth -= 1
	return index
