__all__ = ["stdlib", "operators", "control_flow"]

from . import stdlib
from . import operators
from . import control_flow

libs = [stdlib, operators, control_flow]
exports = {}
for lib in libs:
	for export in lib.exports.keys():
		exports[export] = lib.exports[export]