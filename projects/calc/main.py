import sys
from calc import helper

expr = sys.argv[1]

if(expr == "") or (len(expr.split()) != 3):
    print("Invalid expression. Please provide an expression in the format: <number> <operator> <number>")
    sys.exit(1)

a, op, b = expr.split()

ans =  helper(a, b, op)
print(ans)