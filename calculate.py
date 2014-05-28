
operators = {'+', '-', '*', '/', '(', ')'}


def parse_formula(text):

    tokens = []
    buffer = ''

    for c in text:
        if '0' <= c <= '9':
            buffer += c
        elif c in operators:
            if buffer:
                tokens.append(int(buffer))
            tokens.append(c)
            buffer = ''

    if buffer:
        tokens.append(int(buffer))

    return tokens


if __name__ == '__main__':

    import sys

    if len(sys.argv) < 2:
        print('Input formula required')
    else:
        formula = sys.argv[1]

        print('tokens={}'.format(parse_formula(formula)))


