import statistics

with open('data.txt','r') as file:
    lines = file.readlines()
    
xValues = []
yValues = []
for index ,line  in enumerate(lines):
    try:
        number = int(line.strip())
        xValues.append(index)
        yValues.append(number)
    except ValueError:
        continue
print("x values:",xValues)
print("y values", yValues)