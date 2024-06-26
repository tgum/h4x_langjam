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
def import_module(scope, name, prefix=""):
	module = importlib.import_module(name)
	for key in module.exports.keys():
		scope[prefix + key] = module.exports[key]
	return scope
