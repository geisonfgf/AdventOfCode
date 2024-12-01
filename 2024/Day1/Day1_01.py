def read_input_file(file_path):
    left_list = []
    right_list = []

    # Read the file and populate the left and right lists
    with open(file_path, "r") as file:
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)

    return left_list, right_list


def calculate_total_distance(left_list, right_list):
    # Sort both lists in ascending order
    left_list.sort()
    right_list.sort()

    # Calculate the total distance between paired elements
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

    return total_distance


# Read input data from input.txt
file_path = "input.txt"
left_list, right_list = read_input_file(file_path)

# Calculate and print the total distance
total_distance = calculate_total_distance(left_list, right_list)
print("Total distance:", total_distance)
