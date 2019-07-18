def compute(input_string):
    values = input_string.split(' ')
    num0 = int(values[0])
    num1 = int(values[2])
    operator = values[1]
    if operator == '+':
        return num0 + num1
    else:
        raise ValueError('Unknown operator!')

print(compute('1 + 5'))

