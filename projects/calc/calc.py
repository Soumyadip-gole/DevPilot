def helper(a, b, op):
    a = int(a)
    b = int(b)
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    elif op == "%":
        return a % b
    else:
        return "Unsupported operator"