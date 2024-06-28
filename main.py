from pprint import pprint

import h4x

with open("tests/numbers.h4x", "r") as f:
	program = f.read()


scopes = h4x.create_scopes()
h4x.import_module(scopes[0], "h4x.stdlib")

parsed = h4x.parse(program)
evaled = h4x.eval(parsed, scopes)
print(evaled)
