from sympy import *
x = symbols('x')
print(solve(18750*x+0.026*ln(x/5e-13)-0.45))