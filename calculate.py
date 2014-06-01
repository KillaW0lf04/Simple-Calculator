#! /usr/bin/python3m

__author__ = 'Michael Aquilina'

__desc__ = \
    """
    Simple script that is able to parse and solve input formulas from the command line.
    This is performed by transforming the formula to postfix (Reverse-Polish) notation.
    Contains support for all standard operators including:
    * Multiplication
    * Division
    * Addition
    * Subtraction
    * Modulus
    Ambiguous formulas are solved using standard BODMAS rules. Parentheses are also
    supported to specify exact orderings.
    """

from string import whitespace

# List of operators along with their associated precedence
operators = {'+': 3, '-': 3, '%': 2, '*': 2, '/': 2, '(': 1, ')': 1}


def operation(v1, v2, operator):
    if operator == '+':
        return v1 + v2
    elif operator == '-':
        return v1 - v2
    elif operator == '*':
        return v1 * v2
    elif operator == '/':
        return float(v1 / v2)
    elif operator == '%':
        return v1 % v2
    else:
        raise ValueError('Unknown operator specified: {}'.format(operator))


def parse_formula(text):

    tokens = []
    buffer = ''

    for c in text:
        if '0' <= c <= '9' or c == '.':
            buffer += c
        elif c in operators:
            if buffer:
                tokens.append(float(buffer))
            tokens.append(c)
            buffer = ''
        elif c in whitespace and buffer:
            tokens.append(float(buffer))
            buffer = ''

    if buffer:
        tokens.append(float(buffer))

    return tokens


def calculate(formula):
    tokens = parse_formula(formula)

    operator_stack = []
    operand_stack = []

    for item in tokens:
        if type(item) is float:
            operand_stack.append(item)
        elif type(item) is str:

            if operator_stack:
                peek = operator_stack[-1]
            else:
                peek = None

            if item == ')':
                item = operator_stack.pop()

                while item != '(':
                    value2 = operand_stack.pop()
                    value1 = operand_stack.pop()

                    operand_stack.append(operation(value1, value2, item))

                    item = operator_stack.pop()

            elif peek is None or peek == '(' or operators[item] <= operators[peek]:
                operator_stack.append(item)
            else:
                value2 = operand_stack.pop()
                value1 = operand_stack.pop()

                operand_stack.append(operation(value1, value2, item))
        else:
            raise ValueError('Unknown item found in tokens')

    while operator_stack:
        item = operator_stack.pop()
        value2 = operand_stack.pop()
        value1 = operand_stack.pop()

        operand_stack.append(operation(value1, value2, item))

    return operand_stack.pop()


if __name__ == '__main__':

    import sys

    if len(sys.argv) < 2:
        print('Usage: ')
        print('    python calculate.py <formula>')
        print(__desc__)
    else:
        text = ' '.join(sys.argv[1:])

        print(text)
        print(calculate(text))
