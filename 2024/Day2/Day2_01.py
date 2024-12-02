# Read the input data from the file
file_path = 'input.txt'
with open(file_path, 'r') as file:
    reports = [list(map(int, line.strip().split())) for line in file.readlines()]


# Function to check if a report is safe
def is_safe_report(report):
    if len(report) < 2:
        return False

    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are either increasing or decreasing
    # and within the range [1, 3] or [-3, -1]
    all_increasing = all(1 <= diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return all_increasing or all_decreasing


# Count the number of safe reports
safe_count = sum(is_safe_report(report) for report in reports)

# Output the result
print(safe_count)
