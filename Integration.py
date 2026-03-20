# damn here we are here again
from sympy import Symbol, integrate, sympify, sin, cos, log, ln, exp, tan, oo, sec, csc, cot, asin, acos, atan, acsc, asec, acot
x = Symbol('x')
# This is just a integration machine. 
Message = input(" Enter function (F) : ")
# sympify is here to convert to math function language
message = sympify(Message)
print(f" I = {integrate(message)}")