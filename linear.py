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

meanX = statistics.mean(xValues)
meanY = statistics.mean(yValues)
print("x mean:",meanX)
print("y mean", meanY)
tempGradient = 0
tempC = 0
for i in (xValues):
    tempGradient += (xValues[i] - meanX) * (yValues[i]-meanY)
    tempC += (xValues[i] - meanX) ** 2
gradient = tempGradient / tempC
c = meanY - (gradient * meanX)
print("gradient", gradient)
print("c", c)

