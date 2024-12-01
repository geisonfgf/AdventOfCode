from collections import Counter


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


def calculate_similarity_score(left_list, right_list):
    # Step 1: Count the frequency of each number in the right list
    right_count = Counter(right_list)

    # Step 2: Calculate the similarity score
    similarity_score = sum(left * right_count[left] for left in left_list)

    return similarity_score


# Read input data from input.txt
file_path = "input.txt"
left_list, right_list = read_input_file(file_path)

# Calculate and print the similarity score
similarity_score = calculate_similarity_score(left_list, right_list)
print("Similarity score:", similarity_score)
