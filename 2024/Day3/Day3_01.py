import re


def calculate_mul_sum(file_path):
    # Read the input file
    with open(file_path, 'r') as file:
        data = file.read()

    # Regular expression to find valid mul(X,Y) patterns
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, data)

    # Compute the sum of all valid multiplication results
    total_sum = sum(int(x) * int(y) for x, y in matches)

    return total_sum


# File path to the input data
file_path = 'input.txt'

# Calculate the sum of all valid mul(X,Y) results
result = calculate_mul_sum(file_path)
print("Sum of all valid multiplications:", result)
