def compute(input_string):
    """
    This is my docstring for this function. I don't
    feel like writing much here.
    """


    values = input_string.split(' ')
    num0 = int(values[0])
    num1 = int(values[2])
    operator = values[1]
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    else:
        raise ValueError('Unknown operator!')

