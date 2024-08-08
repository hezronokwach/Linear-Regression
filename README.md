# Linear Statistics Calculator
![image](https://images.prismic.io/turing/652ebbb1fbd9a45bcec81804_Linear_regression_algorithm_11zon_8506fa7116.webp?auto=format,compress)

This Python script calculates the linear regression line and Pearson correlation coefficient for a given set of data. It reads data from a file, performs the necessary calculations, and prints the results.
## Features

Reads numerical data from a file.

Calculates the linear regression line.

Calculates the Pearson correlation coefficient.

## Usage
Ensure you have Python3 installed on your system.

Prepare a text file (data.txt) containing your data, with one number per line.

 Run the script from the command line:
```bash
python3 linear.py data.txt
```
## How to Test the Program
Create a text file named data.txt and populate it with integers, one per line. For example:

```bash
189
113
121
114
145
110
```
Run the script with the data file as an argument:
```bash
python3 linear.py data.txt
```
The script will output the linear regression(6d.p) line and the Pearson correlation coefficient(10d.p).
```bash
Linear Regression: y = -8.742857x + 153.857143
Pearson Correlation Coefficient: -0.5330331012
```

## Linear Regression Line

The linear regression line is a straight line that best fits the data points. It is represented by the equation:
![linear equation](https://latex.codecogs.com/svg.image?$$y=mx&plus;c$$)

Where:

y is the dependent variable.

x is the independent variable.

m is the gradient of the line.

c is the y-intercept.

## Calculation in the Program

The script calculates the slope (m) and intercept (c) using the formulas:

For the gradient \( m \):

![gradient](https://latex.codecogs.com/svg.image?$$m=%5Cfrac%7B%5Csum%7B(x_i-%5Cbar%7Bx%7D)(y_i-%5Cbar%7By%7D)%7D%7D%7B%5Csum%7B(x_i-%5Cbar%7Bx%7D)%5E2%7D%7D$$)

For the intercept \( c \):

![intercept](https://latex.codecogs.com/svg.image?$$c=%5Cbar%7By%7D-m%5Cbar%7Bx%7D$$)

Where:

![barx](https://latex.codecogs.com/svg.image?$%5Cbar%7Bx%7D$) and ![bary](https://latex.codecogs.com/svg.image?$%5Cbar%7By%7D$) are the means of the x  and y values, respectively.

![xi](https://latex.codecogs.com/svg.image?$x_i$) and ![yi](https://latex.codecogs.com/svg.image?$y_i$) are the current values of x and y

## Pearson correlation coefficient

The Pearson correlation coefficient  \( r \) measures the strength and direction of the linear relationship between two variables. It ranges from -1 to 1, where:

    1 indicates a perfect positive linear relationship.
    -1 indicates a perfect negative linear relationship.
    0 indicates no linear relationship.

## Calculation in the Program

The script calculates the Pearson correlation coefficient using the formula:

For the Pearson correlation coefficient \( r \):

![Pearson Correlation Coefficient](https://latex.codecogs.com/svg.latex?r%20%3D%20%5Cfrac%7B%5Ctext%7Bcov%7D%28x%2C%20y%29%7D%7B%5Csigma_x%20%5Csigma_y%7D)

Where:
- ![covxy](https://latex.codecogs.com/svg.image?$%5Ctext%7Bcov%7D(x,y)$) is the covariance of x and y,
- ![sigmax](https://latex.codecogs.com/svg.image?$%5Csigma_x$) is the standard deviation of x,
- ![sigmay](https://latex.codecogs.com/svg.image?$%5Csigma_y$) is the standard deviation of y.

The covariance ![covxy](https://latex.codecogs.com/svg.image?$%5Ctext%7Bcov%7D(x,y)$) is calculated by:

![Covariance](https://latex.codecogs.com/svg.image?$$%5Ctext%7Bcov%7D(x,y)=%5Cfrac%7B%5Csum%7B(x_i-%5Cbar%7Bx%7D)(y_i-%5Cbar%7By%7D)%7D%7D%7Bn-1%7D$$)

Where:

n is the total number of data entries

![barx](https://latex.codecogs.com/svg.image?$%5Cbar%7Bx%7D$) and ![bary](https://latex.codecogs.com/svg.image?$%5Cbar%7By%7D$) are the means of the x  and y values, respectively.
![xi](https://latex.codecogs.com/svg.image?$x_i$) and ![yi](https://latex.codecogs.com/svg.image?$y_i$) are the current values of x and y

## Script Explanation

The script consists of the following main functions:

 read_data(file_path): Reads the data from the file and returns two lists: x_values (indices) and y_values (data points).

calculate_statistics(x_values, y_values): Calculates the mean of x_values and y_values, the slope (gradient), the intercept, and the Pearson correlation coefficient.

main(file_path): The main function that reads the data, calculates the statistics, and prints the results.

Command-Line Interface: The script takes one command-line argument, the file path, and validates the input.

## License

This project is licensed under the MIT License.

## Author
[Hezron Okwach](https://github.com/hezronokwach) 