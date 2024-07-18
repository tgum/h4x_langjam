__all__ = ["tokens", "lexer", "parser", "datatypes", "runner"]

import importlib

import sys

from . import error
from . import tokens
from . import lexer
from . import parser
from . import datatypes
from . import runner

DEBUG = False

program = ""

DEBUG_last_token = None
DEBUG_scopes = []

tokenize = lexer.tokenize
tokens_to_tree = parser.parse
eval = runner.eval

PATH = ["h4x.stdlib."]

def import_module(scope, name):
	path_save = sys.path
	#sys.path = PATH

	found = False
	for path in reversed(PATH):
		try:
			print(f"tring to find {path+name}")
			module = importlib.import_module(path+name, ".")
			for key in module.exports.keys():
				scope[key] = module.exports[key]

			print(f"found in {path}")
			found = True
			break
		except ModuleNotFoundError:
			pass

	if not found:
		raise ImportError(f"Couldn't find module \"{name}\" in path {PATH}")
	
	sys.path = path_save
	return scope
	
	#spec = importlib.util.find_spec(f"{name}", None if path == "" else path)
def import_stdlib(scopes):
		module = importlib.import_module("h4x.stdlib")
		for key in module.exports.keys():
			scopes[0][key] = module.exports[key]

def make_trace(scope):
	return {"scope": scope, "token": DEBUG_last_token}
def create_scopes():
	scopes = [{}]
	scopes[0]["*trace"] = make_trace("Program")
	return scopes

def parse(prog):
	tokens = tokenize(prog)
	return tokens_to_tree(tokens)

def run(program):
	scopes = create_scopes()

	import_module(scopes[0], "h4x.stdlib")
	
	parsed = parse(program)
	evaled = eval(parsed, scopes)
	return evaled
