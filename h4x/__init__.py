__all__ = ["tokens", "lexer", "parser", "datatypes", "runner"]

import importlib

from . import tokens
from . import lexer
from . import parser
from . import datatypes
from . import runner

tokenize = lexer.tokenize
parse = parser.parse
eval = runner.eval

PATH = ["", "h4x.stdlib."]

def import_module(scope, name, prefix=""):
	path = None
	for path in PATH:
		spec = importlib.util.find_spec(path+name, path)
		if spec:
			break
	if path != None:
		module = importlib.import_module(path + name)
		for key in module.exports.keys():
			scope[key] = module.exports[key]
		return scope
