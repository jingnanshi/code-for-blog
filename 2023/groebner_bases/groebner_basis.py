from sympy import groebner
from sympy.abc import x, y, z

F = [x+z, y-z]
groebner(F, x, y, order='lex')
