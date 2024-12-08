import re


def calculate_enabled_mul_sum(file_path):
    # Read the input file
    with open(file_path, 'r') as file:
        data = file.read()

    # Regular expressions to match instructions
    mul_pattern = r'mul\((\d+),(\d+)\)'
    control_pattern = r'\b(do|don\'t)\(\)'

    # State: mul instructions start as enabled
    mul_enabled = True
    total_sum = 0

    # Tokenize the file based on recognized patterns
    tokens = re.findall(f'{mul_pattern}|{control_pattern}', data)

    for token in tokens:
        if token[0] and token[1]:  # It's a mul(X,Y) instruction
            if mul_enabled:
                x, y = int(token[0]), int(token[1])
                total_sum += x * y
        elif token[2]:  # It's a control instruction (do() or don't())
            if token[2] == 'do':
                mul_enabled = True
            elif token[2] == "don't":
                mul_enabled = False

    return total_sum


# File path to the input data
file_path = 'input.txt'

# Calculate the sum of all enabled mul(X,Y) results
result = calculate_enabled_mul_sum(file_path)
print("Sum of all enabled multiplications:", result)
