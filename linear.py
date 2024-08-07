import statistics
import sys

def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    x_values = []
    y_values = []
    for index, line in enumerate(lines):
        try:
            number = int(line.strip())
            x_values.append(index)
            y_values.append(number)
        except ValueError:
            continue
    
    return x_values, y_values

def calculate_statistics(x_values, y_values):
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
    pc = temp_grad / (len(x_values) - 1)
    
    return gradient, c, pc

def main(file_path):
    x_values, y_values = read_data(file_path)
    gradient, c, pc = calculate_statistics(x_values, y_values)
    
    print("y = <%.6f>x + <%.6f>" % (gradient, c))
    print("<%.10f>" % (pc))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <file_path>")
        exit
    else:
        file_path = sys.argv[1]
        main(file_path)
