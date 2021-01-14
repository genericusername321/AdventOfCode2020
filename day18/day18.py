# Advent of Code day 18

def findPrecedence(op):

    if op == '+':
        return 2 
    elif op == '*':
        return 1
    else: return None

def parse(expression):
    # Parse arithmetic expression using Shunting-Yard algorithm.
    # The arithmetic expression is given as a list where each element is a number
    # or an operator (+, *, (, ))

    operators = ['+', '*', '(', ')']

    output = []     # Output stack
    opStack = []  # Operator stack

    exp = expression[::-1]
    while exp:
        token = exp.pop()
        if token in {'+', '*'}:
            # Clear out operator stack until '(' then push to operator stack
            while opStack and opStack[-1] != '(' and \
            findPrecedence(token) <= findPrecedence(opStack[-1]):

                output.append(opStack.pop())

            opStack.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            while opStack[-1] != '(':
                op = opStack.pop()
                output.append(op)
            
            # Delete matching '(' parenthesis
            opStack.pop()

        else:
            token = int(token)
            output.append(token)

    while opStack:
        op = opStack.pop()
        output.append(op)

    return output

def evalute(expression):
    # Evalute an expression given in reverse polish notation

    operators = {'*', '+'}
    expr = expression[::-1]
    stack = []

    while expr:
        token = expr.pop()
        if token in operators:
            a = stack.pop()
            b = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '*':
                stack.append(a * b)

        else:
            stack.append(token)

    return stack[0]

if __name__ == "__main__":

    total = 0

    with open("day18.in") as f:
        for line in f:
            line = line.strip()
            line = line.replace('(', '( ')
            line = line.replace(')', ' )')
            line = line.split(' ')
            expr = parse(line)
            value = evalute(expr)
            total += value

    print(total)


