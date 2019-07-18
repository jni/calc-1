def compute(input_string):
    """Simple calculator.

    Supports all basic operators and both integer and
    floating point numbers.
    """


    values = input_string.split(' ')
    num0 = float(values[0])
    num1 = float(values[2])
    operator = values[1]
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    elif operator == '*':
        return num0 * num1
    elif operator == '/':
        return num0 / num1
    else:
        raise ValueError(f'Unknown operator: {operator}!')

