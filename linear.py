import statistics
import sys


def read_data(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    if not lines:
        return [], [], True  # Indicates that the file is empty

    x_values = []
    y_values = []
    for index, line in enumerate(lines):
        try:
            number = int(line.strip())
            x_values.append(index)
            y_values.append(number)
        except ValueError:
            # Skip invalid entries silently
            continue

    return x_values, y_values, False  # Indicates that the file is not empty


def calculate_statistics(x_values, y_values):
    if len(x_values) < 2:  # Ensure there are enough points for calculation
        raise ValueError("Not enough valid data points for statistics.")

    mean_x = statistics.mean(x_values)
    mean_y = statistics.mean(y_values)

    temp_gradient = 0
    temp_c = 0
    for i in range(len(x_values)):
        temp_gradient += (x_values[i] - mean_x) * (y_values[i] - mean_y)
        temp_c += (x_values[i] - mean_x) ** 2

    gradient = temp_gradient / temp_c
    c = mean_y - (gradient * mean_x)

    temp_grad = 0
    for i in range(len(x_values)):
        temp_grad += (x_values[i] - mean_x) * (y_values[i] - mean_y)
    covxy = temp_grad / (len(x_values) - 1)

    stdev_x = statistics.stdev(x_values)
    stdev_y = statistics.stdev(y_values)
    stdev = stdev_x * stdev_y
    if stdev == 0:
        raise ValueError("Standard deviation cannot be zero.")

    pc = covxy / stdev

    return gradient, c, pc


def main(file_path):
    if not file_path == "data.txt":
        print("Usage: python3 linear.py <data.txt>")
        return
    x_values, y_values, is_empty = read_data(file_path)

    if is_empty:
        print(f"Error: The file '{file_path}' is empty.")
        return
    try:
        gradient, c, pc = calculate_statistics(x_values, y_values)
        print("Linear Regression: y = %.6fx + %.6f" % (gradient, c))
        print("Pearson Correlation Coefficient: %.10f" % (pc))
    except ValueError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 linear.py <data.txt>")
        exit()
    else:
        file_path = sys.argv[1]

    try:
        main(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        exit()
