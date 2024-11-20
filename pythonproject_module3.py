"""#Project Overview
This assignment aims to provide a comprehensive understanding of Python programming fundamentals.

Covered Concepts:

1)Python Functions

2)Lambda Functions

3)NumPy

4)Pandas

5)If Statements

6)Loops (for and while)

7)Lists, Tuples, Sets, Dictionaries

8)Operators (arithmetic, comparison, logical, etc.)

9)Reading CSV files

10)Python String Methods

#1)Python Functions.

a)Create functions with different numbers of parameters and return types.
"""

def multiply_values(x,y):
    z = x * y
    return z

print(multiply_values(3,4))

def findvolume(length=1, width=1, depth=1):
  #print("Length = " + str(length))
  #print("Width = " + str(width))
  #print("Depth = " + str(depth))
  return length * width * depth;

findvolume(1, 2, 3)
findvolume(length=5, depth=2, width=4)
findvolume(2, depth=3, width=4)

def get_name_and_age():
    name = "Sucharitha"
    age = 25
    return name, age

person_name, person_age = get_name_and_age()
print(person_name, person_age)

"""b)Explore function scope and variable accessibility.

A variable is only available from inside the region it is created. This is called scope.

Local Scope: A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

Global Scope: A variable created in the main body of the Python code is a global variable and belongs to the global scope. Global variables are available from within any scope, global and local.

Global Keyword: If you need to create a global variable, but are stuck in the local scope, you can use the global keyword. The global keyword makes the variable global.

Nonlocal Keyword: The nonlocal keyword is used to work with variables inside nested functions. The nonlocal keyword makes the variable belong to the outer function.
"""

#Local Scope
def myfunc():
  a = 15
  print(a)

myfunc()

#Global Scope
firstName = "Sucharitha"
lastName = "Kota"

def myfunc():
  print(firstName+" "+lastName  )

myfunc()

print(firstName)
print(lastName)

#Global Keyword

def myfunc():
 global a
 a="awesome"

myfunc()
print(a)

#Nonlocal Keyword:

def myfunc1():
  b = 4
  def myfunc2():
    nonlocal b
    b = 5
  myfunc2()
  return b

print(myfunc1())

""" c)Functions with default argument values."""

def convert_temperature(value, to_unit="Fahrenheit"):
    if to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif to_unit == "Celsius":
        return (value - 32) * 5/9
    else:
        return "Unknown unit"

print(convert_temperature(30))
print(convert_temperature(86, "Celsius"))

"""d)Write recursive functions."""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6)) # Output: 8 (0, 1, 1, 2, 3, 5, 8)

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print(power(2, 3))

"""e)Demonstrate how to use docstrings to document functions.

In Python, docstrings are a convenient way to document functions, classes, and modules. A docstring is a string that appears as the first statement in a function, method, or class definition. It is used to describe the purpose and behavior of the function. Docstrings are enclosed in triple quotes ('''...'''), and they can span multiple lines.
"""

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    The factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n.
    For example: 5! = 5 * 4 * 3 * 2 * 1 = 120.

    Args:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the input integer n.

    Raises:
        ValueError: If n is a negative integer.

    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))

"""#2) Lambda Functions.

Lambda functions in Python are small, anonymous functions defined using the lambda keyword. They can take any number of arguments but only have one expression, which is evaluated and returned.

a)Create simple lambda functions for various operations.
"""

# Add two numbers
add = lambda x, y: x + y
print(add(3, 5))

#function to check even number
is_even = lambda x: x % 2 == 0
print(is_even(4))
print(is_even(7))

#Function to check the square of a number
square = lambda x: x ** 2
print(square(4))

#Concate Strings
concat = lambda a, b: a + b
print(concat("Hello, ", "World!"))  # Output: "Hello, World!"

"""b)Use lambda functions with built-in functions like map, filter, and reduce.

Lambda functions are powerful tools in Python that can be used effectively with built-in functions like map, filter, and reduce. These combinations allow for concise and efficient data manipulation.
"""

#Map function with Lambda
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))

print(doubled_numbers)

#Filter function with Lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

#Reduce function with lambda
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)

print(product)

"""c)Compare lambda functions with regular functions in terms of syntax and use cases.

Lambda functions and regular functions (defined using def) are both used to define functions in Python, but they differ in several ways, including syntax, use cases, and functionality.

Regular Functions:

Regular functions are defined using the def keyword. They are more versatile and can contain multiple expressions and statements, including conditionals, loops, and return statements.

lambda Functions:

Lambda functions are short, anonymous functions defined using the lambda keyword. They are typically used for small, throwaway functions that can be defined in a single line.
"""

#Regular Function in Sorting
def get_second_element(pair):
    return pair[1]

pairs = [(1, 2), (3, 1), (5, 4), (2, 3)]
sorted_pairs = sorted(pairs, key=get_second_element)
print(sorted_pairs)

#Lambda Function in Sorting
pairs = [(1, 2), (3, 1), (5, 4), (2, 3)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)

"""#3) Numpy

NumPy is a Python library used for working with arrays.It also has functions for working in domain of linear algebra, fourier transform, and matrices.NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

NumPy stands for Numerical Python.

a)Create different types of NumPy arrays (1D, 2D, 3D).
"""

#Creating 1D array with numpy
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#Creating 2D array with numpy
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

#Creating 3D array with numpy
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

"""b)Perform basic arithmetic operations on arrays."""

import numpy as np
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])

# 1D Array Addition
sum_1d = arr1 + arr2
print("1D Array Addition:")
print(sum_1d)

# 2D Array Addition
sum_2d = arr3 + arr4
print("\n2D Array Addition:")
print(sum_2d)

# 1D Array Subtraction
diff_1d = arr1 - arr2
print("1D Array Subtraction:")
print(diff_1d)

# 2D Array Subtraction
diff_2d = arr3 - arr4
print("\n2D Array Subtraction:")
print(diff_2d)


# 1D Array Multiplication
prod_1d = arr1 * arr2
print("1D Array Multiplication:")
print(prod_1d)

# 2D Array Multiplication
prod_2d = arr3 * arr4
print("\n2D Array Multiplication:")
print(prod_2d)

# 1D Array Division
div_1d = arr1 / arr2
print("1D Array Division:")
print(div_1d)

# 2D Array Division
div_2d = arr3 / arr4
print("\n2D Array Division:")
print(div_2d)

"""c)Use indexing and slicing to access elements.

In NumPy, indexing and slicing are powerful tools to access and manipulate array elements. These concepts are similar to Python’s standard indexing and slicing for lists, but NumPy arrays support more advanced functionality like multi-dimensional slicing and advanced indexing.
"""

import numpy as np

# Creating a 1D array
arr_1d = np.array([10, 20, 30, 40, 50])

# Accessing elements by index
print("Element at index 0:", arr_1d[0])  # 10
print("Element at index 2:", arr_1d[2])  # 30
print("Element at index -1 (last element):", arr_1d[-1])  # 50

# Slicing a 1D array
print("Slice from index 1 to 3:", arr_1d[1:4])  # [20, 30, 40]
print("Slice from the beginning to index 2:", arr_1d[:3])  # [10, 20, 30]
print("Slice from index 2 to the end:", arr_1d[2:])  # [30, 40, 50]
print("Slice with step (every second element):", arr_1d[::2])  # [10, 30, 50]

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Accessing elements by row and column
print("Element at row 0, column 1:", arr_2d[0, 1])  # 2
print("Element at row 2, column 2:", arr_2d[2, 2])  # 9

# Slicing rows and columns in a 2D array
print("Slice rows 0 to 1, columns 1 to 2:", arr_2d[0:2, 1:3])
# Output: [[2 3]
#          [5 6]]

# Slicing the entire second column
print("Second column:", arr_2d[:, 1])  # [2, 5, 8]

# Slicing the entire second row
print("Second row:", arr_2d[1, :])  # [4, 5, 6]

"""d)Explore array manipulation functions (reshape, transpose, concatenate).


NumPy provides several powerful functions to manipulate arrays. These functions allow you to modify the shape, order, and composition of arrays efficiently. Below, I'll explore three key array manipulation functions in NumPy.
"""

import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape the array into a 2x6 matrix (2 rows and 6 columns)
reshaped_arr = arr.reshape(2, 6)
print("Reshaped Array (2x6):")
print(reshaped_arr)

# Reshape the array into a 3x4 matrix (3 rows and 4 columns)
reshaped_arr_2 = arr.reshape(3, 4)
print("\nReshaped Array (3x4):")
print(reshaped_arr_2)

# Create a 2D array (matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Transpose the 2D array (swap rows and columns)
transposed_arr = arr_2d.T
print("Transposed Array (2D):")
print(transposed_arr)

# Transpose a higher-dimensional array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
transposed_3d = arr_3d.transpose(1, 0, 2)  # Change the order of axes
print("\nTransposed 3D Array:")
print(transposed_3d)


# Create two 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenate along axis 0 (join arrays end-to-end)
concatenated_1d = np.concatenate((arr1, arr2), axis=0)
print("Concatenated 1D Array:")
print(concatenated_1d)

# Create two 2D arrays
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[7, 8, 9], [10, 11, 12]])

# Concatenate along axis 0 (rows)
concatenated_2d_axis0 = np.concatenate((arr3, arr4), axis=0)
print("\nConcatenated 2D Array along axis 0:")
print(concatenated_2d_axis0)

# Concatenate along axis 1 (columns)
concatenated_2d_axis1 = np.concatenate((arr3, arr4), axis=1)
print("\nConcatenated 2D Array along axis 1:")
print(concatenated_2d_axis1)

"""e)Create and use NumPy random number generators.

NumPy provides the numpy.random module, which allows you to generate random numbers and perform random sampling from a variety of distributions. The module includes functions to generate random numbers from uniform distributions, normal distributions, and others, as well as to shuffle and sample elements randomly.


"""

import numpy as np

# Generate a single random integer between 0 and 10
rand_int = np.random.randint(0, 10)
print("Random Integer:", rand_int)

# Generate an array of 5 random integers between 1 and 100
rand_int_arr = np.random.randint(1, 100, size=5)
print("Random Integer Array:", rand_int_arr)

"""#4)Pandas

Pandas is a Python library used for working with data sets.It has functions for analyzing, cleaning, exploring, and manipulating data.The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.
Pandas allows us to analyze big data and make conclusions based on statistical theories.Pandas can clean messy data sets, and make them readable and relevant.
Relevant data is very important in data science.

a)Create Pandas Series and DataFrames.

"""

import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print("Series from list:")
print(series)

# Create a DataFrame from a dictionary
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data_dict)

print("DataFrame from dictionary:")
print(df)

"""b)Load data from various file formats (CSV, Excel, etc.).

Pandas provides convenient functions to load data from various file formats such as CSV, Excel, JSON, and more. Below, I'll demonstrate how to load data from several common file formats including CSV, Excel.
"""

import pandas as pd

# Load data from a CSV file
df_csv = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv")

print("Data loaded from CSV:")
print(df_csv.head())  # Display the first 5 rows

import pandas as pd
df_csv = pd.read_json("https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json")
print("Data loaded from JSON:")
print(df_csv.head())

"""c)Perform data cleaning and manipulation tasks.

Data cleaning and manipulation are essential steps in the data analysis process. These tasks involve cleaning the dataset, handling missing values, removing duplicates, converting data types, and applying transformations to the data to make it ready for analysis.


"""

import pandas as pd

# Load data from a CSV file
df = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv')  # Replace with your file path

# Display the first few rows
print(df.head())

# Check for missing values in each column
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Fill missing values with a constant (e.g., 0)
df_filled = df.fillna(0)

# Display the cleaned DataFrame
print(df_filled)

# Drop rows with any missing values
df_dropped = df.dropna()

# Drop columns with any missing values
df_dropped_columns = df.dropna(axis=1)

print(df_dropped.head())

# Identify duplicate rows
duplicates = df.duplicated()

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

print(df_no_duplicates.head())

# Rename columns
df_renamed = df.rename(columns={'Name': 'full_Name'})

print(df_renamed.head())

"""d)Explore data analysis and visualization using Pandas.

Pandas is not only a powerful tool for data cleaning and manipulation, but it also provides excellent features for data analysis and visualization.


"""

#Basic Data analysis using pandas
import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
})

# Get descriptive statistics for numerical columns
print(df.describe())

df2 = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
})

# Group by 'City' and calculate the mean of 'Age' and 'Salary'
df_grouped = df2.groupby('City').agg({'Age': 'mean', 'Salary': 'mean'})
print(df_grouped)

#Basic Visualizations using pandas
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Davis', 'Charlie Brown',
             'David Wilson', 'Emily Clark', 'Frank White', 'Grace Lee', 'Henry Scott'],
    'Department': ['HR', 'Finance', 'Engineering', 'Marketing', 'HR',
                   'Finance', 'Engineering', 'Marketing', 'HR', 'Finance'],
    'Salary': [50000, 60000, 75000, 55000, 48000, 70000, 80000, 62000, 54000, 72000]
}

# Display the first few rows to verify the data
print(df.head())

# Group the data by 'Department' and calculate the total salary per department
department_salary = df.groupby('Department')['Salary'].sum()

# Plotting the Bar Chart
plt.figure(figsize=(10, 6))  # Set figure size
department_salary.plot(kind='bar', color='skyblue')

# Adding title and labels
plt.title('Total Salary by Department', fontsize=16)
plt.xlabel('Department', fontsize=12)
plt.ylabel('Total Salary', fontsize=12)

# Rotating x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()  # Adjust layout for better spacing
plt.show()

"""e)Create pivot tables and group data for analysis.

Creating pivot tables and grouping data are essential techniques for summarizing and analyzing data, especially when you need to extract insights from large datasets.
"""

import pandas as pd

# Sample DataFrame
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Department': ['HR', 'Engineering', 'HR', 'Engineering', 'Sales'],
    'Salary': [60000, 80000, 65000, 85000, 50000],
    'Age': [25, 30, 35, 40, 22]
}

df = pd.DataFrame(data)
display(df)


#Basic Pivot table
pivot_table = df.pivot_table(values='Salary', index='Age', columns='Department', aggfunc='mean')

print(pivot_table)

"""#5)IF Statements

Python supports the usual logical conditions from mathematics:

Equals: a == b

Not Equals: a != b

Less than: a < b

Less than or equal to: a <= b

Greater than: a > b

Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

a)Demonstrate conditional logic using if, else, and elif statements.

"""

#If statment
num = 5

if num > 0:
    print("The number is positive.")

#If-else statment
num = -3

if num > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

#elif statement
num = 0

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

"""b)Create complex conditional expressions.

In Python, you can combine multiple conditions to create complex conditional expressions using logical operators like and, or, not, and parentheses to group conditions. Complex conditional expressions allow you to evaluate multiple conditions simultaneously and make more refined decisions in your program.

"""

#Checking the number in-between and even
num = 18

if num >= 10 and num <= 20 and num % 2 == 0:
    print("The number is between 10 and 20 and is even.")
else:
    print("The number does not meet the conditions.")

#Number is positive or greater than threshold
num = 50
threshold = 100

if num > 0 or num > threshold:
    print("The number is positive or greater than the threshold.")
else:
    print("The number is neither positive nor greater than the threshold.")

#Checking the number in between the range or greater
num = 15
min_range = 10
max_range = 20
threshold = 25

if (num >= min_range and num <= max_range) or num > threshold:
    print("The number is within the range or greater than the threshold.")
else:
    print("The number is outside the range and below the threshold.")

"""c)Implement nested if statements.

A nested if statement occurs when you place one if statement inside another. This allows you to check for multiple conditions in a structured way, where one condition depends on the result of another condition. Nested if statements are useful when you need to evaluate more complex logic that involves multiple levels of decision-making.
"""

num = 14

if num > 0:  # Check if the number is positive
    if num % 2 == 0:  # Nested check to see if the number is even
        print(f"{num} is a positive and even number.")
    else:  # This block runs if the number is positive but odd
        print(f"{num} is a positive but odd number.")
else:
    print(f"{num} is not a positive number.")

"""#6)Loops

Loops are essential constructs in programming that allow you to repeat a block of code multiple times. In Python, the two most commonly used types of loops are the for loop and the while loop. Both serve different purposes, but they can often be used interchangeably depending on the situation.

a)Use for loops to iterate over sequences.
"""

#Looping over list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#nested loops
#Generate all combinations of pairs from a list of items.
def generate_combinations(items):

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            print(f"({items[i]}, {items[j]})")

# Example usage
generate_combinations(['d', 'r', 'a'])

#Looping over multiple sequences.
names = ["John", "Alice", "Bob"]
ages = [30, 25, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

"""b)Employ while loops for indefinite iteration.

A while loop in Python is used for indefinite iteration—meaning that the loop continues to execute as long as a specified condition remains True. This is particularly useful when you do not know in advance how many iterations are needed but rather want the loop to continue until a certain condition is met.
"""

while True:  # Infinite loop
    user_input = input("Type 'exit' to stop: ")
    if user_input.lower() == 'exit':  # Exit the loop if the user types 'exit'
        print("Exiting the loop.")
        break
    else:
        print("You typed:", user_input)

"""c)Implement nested loops.

A nested loop is a loop inside another loop. In Python, this can involve placing a for loop or a while loop inside another for or while loop. Nested loops are particularly useful for working with multi-dimensional data structures like matrices or performing complex iterations where one loop depends on the other.
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:  # Outer loop iterates through each row
    for element in row:  # Inner loop iterates through each element in the row
        print(element, end=" ")  # Print elements in the same line
    print()  # New line after each row

# Printing a triangle pattern
for i in range(1, 6):  # Outer loop controls number of rows
    for j in range(i):  # Inner loop prints stars based on row number
        print("*", end=" ")
    print()  # New line after each row

# 3D list (list of lists of lists)
three_d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

for matrix in three_d:  # Outer loop for each 2D matrix
    for row in matrix:  # Middle loop for each row
        for element in row:  # Inner loop for each element in the row
            print(element, end=" ")
        print()  # New line after each row
    print()  # New line after each matrix

"""d)Utilize break and continue statements.

The break and continue statements are control flow tools that allow you to alter the behavior of loops (for and while). These statements give you more control over how loops behave under specific conditions.
"""

numbers = [4, 6, 8, 9, 11, 13, 15, 17]

for number in numbers:
    if number < 2:  # Skip numbers less than 2 (they are not prime)
        continue
    for i in range(2, number):  # Check for divisibility from 2 to number-1
        if number % i == 0:  # If the number is divisible by any number in the range, it's not prime
            break  # Exit the inner loop
    else:
        # This else is associated with the for-loop, not the if-statement
        print(f"Prime number found: {number}")
        if number > 10:
            print("Found a prime greater than 10, exiting the loop.")
            break  # Exit the outer loop when a prime greater than 10 is found

# Sample data: List of students with their names and grades
students = [
    {'name': 'John', 'grade': 45},
    {'name': 'Jane', 'grade': 92},
    {'name': 'Bob', 'grade': 73},
    {'name': 'Alice', 'grade': 88},
    {'name': 'Charlie', 'grade': 35},
    {'name': 'David', 'grade': 98}
]

# Initialize a counter to iterate over the list of students
index = 0

# Use a while loop to iterate over the students list
while index < len(students):
    student = students[index]
    print(f"Processing {student['name']}...")

    # If the grade is below 50, it's failing, so skip to the next student
    if student['grade'] < 50:
        print(f"{student['name']} is failing with grade {student['grade']}. Needs improvement!")
        index += 1  # Move to the next student
        continue  # Skip the rest of the loop for this student

    # If the grade is above 90, print 'Excellent' and break out of the loop
    elif student['grade'] > 90:
        print(f"Excellent! {student['name']} has achieved an outstanding grade of {student['grade']}!")
        break  # Exit the loop completely after encountering an excellent grade

    # Otherwise, print the student's grade
    else:
        print(f"{student['name']} has a grade of {student['grade']}.")

    # Increment the index to process the next student
    index += 1

print("Finished processing all students.")

"""#7)Lists, Tuples, Sets, Dictionaries


1. Lists in Python:

A list is an ordered collection of items which can be of any type. Lists are mutable, meaning their contents can be modified after creation (i.e., elements can be added, removed, or modified).

2. Tuples in Python:

A tuple is an ordered collection of elements, similar to a list, but it is immutable. Once a tuple is created, its elements cannot be changed, added, or removed.


3. Sets in Python:

A set is an unordered collection of unique elements. Sets are mutable, but they do not allow duplicate elements, and their order is not guaranteed.

4. Dictionaries in Python:

A dictionary is an unordered collection of key-value pairs. The keys in a dictionary must be unique, while the values can be of any data type. Dictionaries are mutable.


a)Create and manipulate lists, tuples, sets, and dictionaries.
"""

#Creating and Manipulating Lists
fruits = ["apple", "banana", "cherry"]

# Accessing elements by index
print(fruits[0])

# Slicing the list
print(fruits[1:3])
# Modifying an element
fruits[1] = "orange"
print(fruits)

# Adding an element
fruits.append("grape")
print(fruits)

# Removing an element
fruits.remove("orange")
print(fruits)

#Creating and Manipulating A Tuple
# Creating a tuple
colors = ("red", "green", "blue")

# Accessing elements by index
print(colors[0])

# Slicing the tuple
print(colors[1:3])

#Creating sets in python
numbers = {1, 2, 3, 4, 5}

# Adding an element
numbers.add(6)
print(numbers)

# Removing an element
numbers.remove(3)
print(numbers)

# Sets automatically remove duplicates
numbers = {1, 2, 3, 3, 2, 1}
print(numbers)

# Checking membership
print(4 in numbers)

# Creating a dictionary
person = {"name": "John", "age": 30, "city": "New York"}

# Accessing values by key
print(person["name"])

# Modifying a value
person["age"] = 31
print(person)

# Adding a new key-value pair
person["job"] = "Engineer"
print(person)

# Removing a key-value pair
del person["city"]
print(person)

# Checking if a key exists
print("age" in person)
print("city" in person)

"""b)Understand the differences between these data structures.

Each of the four data structures in Python—lists, tuples, sets, and dictionaries—has distinct characteristics that make them suitable for different use cases.

Differences

Lists:

Ordered collection.
Items are stored in a specific order, and that order is maintained.
Elements can be accessed using their index (e.g., list[0]).
The order of elements in a list is guaranteed (starting from Python 3.7+).


Tuples:

Ordered collection.
Like lists, tuples maintain the order of elements.
Can be accessed via indexing (e.g., tuple[0]).


Sets:

Unordered collection.
The elements do not have a fixed position, so the order of elements is not preserved.
Cannot access elements by index. Elements can only be accessed through iteration.


Dictionaries:

Unordered (until Python 3.7+ where insertion order is preserved).
Data is stored as key-value pairs. Keys are unique, and values are accessed using the key (e.g., dict["key"]).
Insertion order is maintained in Python 3.7+, meaning the items will be returned in the same order they were added.


Use Cases

Lists:

Best used when you need an ordered collection of items that might change.
Ideal for use cases where the order of elements is important, and modifications like adding/removing elements are needed.

Example: Storing a sequence of tasks in a to-do list or a series of steps in a process.

Tuples:

Best used when you need an ordered collection of items that should not be modified.
Ideal for use cases where the integrity of the data should be maintained, and immutability is required (e.g., coordinates, function return values).

Example: Representing fixed data like geographic coordinates (latitude, longitude) or RGB values.

Sets:

Best used when you need a collection of unique items and order doesn't matter.
Ideal for removing duplicates, checking membership, or performing set operations like union, intersection, and difference.

Example: Storing unique items, such as a list of distinct tags or items in a collection.

Dictionaries:

Best used when you need a key-value mapping, with fast lookups by key.
Ideal for associating data that can be accessed quickly via a unique identifier (key).

Example: Storing user information by user ID, or mapping product IDs to product details.

c)Perform operations like indexing, slicing, adding, removing elements.
"""

#indexing with Lists
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])
print(fruits[-1])


#Slicing with lists

print(fruits[1:3])
print(fruits[:2])
print(fruits[2:])

#Adding elements to the list
fruits.append("elderberry")
print(fruits)


fruits.insert(2, "blueberry")
print(fruits)


fruits.extend(["fig", "grape"])
print(fruits)

#Removing elements from the list
fruits.remove("banana")
print(fruits)


fruits.pop(3)
print(fruits)


del fruits[0]
print(fruits)



# indexing, slicing, adding, removing elements with Tuples

coordinates = (10, 20, 30, 40)
print(coordinates[2])
print(coordinates[-1])

# Slicing a tuple
print(coordinates[1:3])
print(coordinates[:2])
print(coordinates[2:])

# Creating a new tuple by concatenating
new_coordinates = coordinates + (50, 60)
print(new_coordinates)



# indexing, removing elements with Sets

my_set = {1, 2, 3, 4}

# Adding a single element
my_set.add(5)
print(my_set)

# Adding multiple elements (using another iterable)
my_set.update([6, 7, 8])
print(my_set)


# Removing a specific element (raises KeyError if element is not present)
my_set.remove(4)
print(my_set)

# Removing an element without raising an error (if element is not found)
my_set.discard(10)

# Removing and returning an arbitrary element
removed_element = my_set.pop()
print(removed_element)
print(my_set)

#sets do not support Indexing and Slicing because they are unordered.

#Adding , Indexing, Slicing and Removing elements with Dictionaries.

person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])
print(person["age"])

# Adding a new key-value pair
person["job"] = "Engineer"
print(person)

# Modifying an existing value
person["age"] = 31
print(person)

# Using pop() to remove a key-value pair and return the value
job = person.pop("job")
print(job)
print(person)

# Using del to remove a key-value pair
del person["city"]
print(person)

# Using popitem() to remove and return the last key-value pair
last_item = person.popitem()
print(last_item)
print(person)

"""d)Explore built-in methods for each data structure.

1)Lists built-in methods.
"""

# Count occurrences
fruit_basket = ['apple', 'banana', 'apple', 'orange', 'apple']
apple_count = fruit_basket.count('apple')
print(f"Number of apples: {apple_count}")

# Find index of an element
banana_index = fruit_basket.index('banana')
print(f"Index of banana: {banana_index}")

# Sort a list
grades = [85, 92, 78, 95, 88]
grades.sort()
print(f"Sorted grades: {grades}")

# Reverse a list
groceries = ['apples', 'milk', 'bread', 'eggs']
groceries.reverse()
print(f"Reversed shopping list: {groceries}")

# Create a copy of a list
expenses = [1200.50, 300.75, 500.00, 150.25]
expenses_copy = expenses.copy()
print(f"Copy of expenses: {expenses_copy}")

"""2)Tuple in-built methods.

"""

# Example Tuple
fruits = ("apple", "banana", "cherry", "apple", "apple", "banana")

# Count occurrences of 'apple'
apple_count = fruits.count("apple")
print(f"The fruit 'apple' appears {apple_count} times.")

#Index with tuple
apple_index = fruits.index("apple")
print(f"The first occurrence of 'apple' is at index {apple_index}.")

"""3)Sets built-in methods.

"""

# Example Set
fruits = {"apple", "banana", "cherry"}

# Adding an element
fruits.add("date")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'date'}

# Adding multiple elements using a list
fruits.update(["cherry", "date", "elderberry"])
print(fruits)

# Removing an element
fruits.remove("banana")
print(fruits)

# Trying to discard an element that doesn't exist will not raise an error
fruits.discard("pear")
print(fruits)

# Popping an arbitrary element
popped_element = fruits.pop()
print(f"Removed element: {popped_element}")
print(f"Remaining set: {fruits}")

# Clearing all elements from the set
fruits.clear()
print(fruits)

# Example Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
union_set = set1.union(set2)
print(union_set)


# Intersection of two sets
intersection_set = set1.intersection(set2)
print(intersection_set)


# Difference of two sets (elements in set1 but not in set2)
difference_set = set1.difference(set2)
print(difference_set)

# Symmetric difference (elements in either set1 or set2, but not both)
symmetric_diff_set = set1.symmetric_difference(set2)
print(symmetric_diff_set)


# Check if set1 is a subset of set2
is_subset = set1.issubset(set2)
print(is_subset)

# Example Sets
set1 = {1, 2, 3, 4}
set2 = {1, 2}

# Check if set1 is a superset of set2
is_superset = set1.issuperset(set2)
print(is_superset)


# Check if set1 and set2 are disjoint
are_disjoint = set1.isdisjoint(set2)
print(are_disjoint)

"""4) Dictionary built-in methods

"""

# Example Dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

# Get the value for 'name'
name = person.get("name")
print(name)

# Get the value for a non-existing key 'gender' with a default value
gender = person.get("gender", "Not Specified")
print(gender)


# Get all the keys
keys = person.keys()
print(keys)


# Get all the values
values = person.values()
print(values)


# Get all the values
values = person.values()
print(values)


# Get all key-value pairs
items = person.items()
print(items)



# Pop an item
name = person.pop("name")
print(name)
print(person)


# Example Dictionaries
person1 = {"name": "Alice", "age": 30}
address = {"city": "New York", "country": "USA"}

# Update 'person' dictionary with 'address'
person1.update(address)
print(person1)

# Example Dictionary
person2 = {"name": "Alice", "age": 30}

# Check if 'city' exists, if not set it to "Unknown"
city = person.setdefault("city", "Unknown")
print(city)
print(person2)

# If the key already exists, no change is made
age = person.setdefault("age", 25)
print(age)


# Example Dictionary
person3 = {"name": "Alice", "age": 30, "city": "New York"}

# Clear all items
person.clear()
print(person3)

# Example Dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

# Make a copy of the dictionary
person_copy = person.copy()
print(person_copy)

# Modify the copy
person_copy["city"] = "Los Angeles"
print(person_copy)
print(person)

# Create a dictionary with keys and default value
keys = ["name", "age", "city"]
default_value = "Unknown"
person = dict.fromkeys(keys, default_value)
print(person)

# Example Dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

# Delete a key-value pair
del person["age"]
print(person)

"""#8)Operators

Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

1)Arithmetic operators

2)Assignment operators

3)Comparison operators

4)Logical operators

5)Identity operators

6)Membership operators

7)Bitwise operators
"""

#Arithmetic operators
a = 10
b = 5

# Addition
sum_result = a + b
print(f"Addition: {a} + {b} = {sum_result}")

# Subtraction
sub_result = a - b
print(f"Subtraction: {a} - {b} = {sub_result}")

# Multiplication
mul_result = a * b
print(f"Multiplication: {a} * {b} = {mul_result}")

# Division (float)
div_result = a / b
print(f"Division: {a} / {b} = {div_result}")

# Floor Division
floor_div_result = a // b
print(f"Floor Division: {a} // {b} = {floor_div_result}")

# Modulus
mod_result = a % b
print(f"Modulus: {a} % {b} = {mod_result}")

# Exponentiation
exp_result = a ** b
print(f"Exponentiation: {a} ** {b} = {exp_result}")

#Comparision Operators

a = 10
b = 5

# Equal to
print(f"Is {a} == {b}? {a == b}")

# Not equal to
print(f"Is {a} != {b}? {a != b}")

# Greater than
print(f"Is {a} > {b}? {a > b}")

# Less than
print(f"Is {a} < {b}? {a < b}")

# Greater than or equal to
print(f"Is {a} >= {b}? {a >= b}")

# Less than or equal to
print(f"Is {a} <= {b}? {a <= b}")

#Logical Operators

a = 10
b = 5
c = 3

# 'and' operator (both conditions must be true)
print(f"Is {a} > {b} and {b} > {c}? {(a > b) and (b > c)}")

# 'or' operator (at least one condition must be true)
print(f"Is {a} > {b} or {b} > {c}? {(a > b) or (b > c)}")

# 'not' operator (negates the condition)
print(f"Is it not true that {a} < {b}? {not (a < b)}")

#Assigment Operators

a = 10
b = 5
c = 3

# Assignment
a = b
print(f"a = b: {a}")

# Add and assign
a += 2
print(f"a += 2: {a}")

# Subtract and assign
a -= 3
print(f"a -= 3: {a}")

# Multiply and assign
a *= 2
print(f"a *= 2: {a}")

# Divide and assign (float division)
a /= 3
print(f"a /= 3: {a}")

# Floor divide and assign
a //= 2
print(f"a //= 2: {a}")

# Modulus and assign
a %= 3
print(f"a %= 3: {a}")

# Exponentiation and assign
a **= 2
print(f"a **= 2: {a}")



# Arithmetic, comparison, and logical operators combined
result = (a + b > c) and (b * c == 15)
print(f"Result of combined operators: {result}")  # Output: True

# Assignment with arithmetic operation
a += b * c  # a = a + (b * c)
print(f"Updated a: {a}")  # Output: 25

"""b)Understand operator precedence.


Operator precedence in Python defines the order in which operators are evaluated in an expression. When multiple operators are involved in an expression, Python uses precedence rules to determine the order in which operations are performed. Operators with higher precedence are evaluated first.
"""

x = 3 + 2 * 5 ** 2 // 3 % 4
print(x)

x = (3 + 2) * 5 ** 2 // 3 % 4
print(x)

"""c)Apply operators in expressions and calculations.

"""

a = 10
b = 5
c = 3

# Combine operators in a single expression
result = a + b * c ** 2 // 3 % 4
print(f"Result of combined operators: {result}")

# Another example with comparison and logical operators
condition = (a > b) and (b == c) or (a == 10)
print(f"Condition result: {condition}")

"""#9)Reading CSV files

a)Read CSV files into Pandas DataFrames.
"""

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv')

# Display the first few rows of the DataFrame
print(df.head())  # This shows the first 5 rows by default

"""b)Explore different CSV reading options and parameters."""

df = pd.read_csv('biostats.csv')  # Local file path
print(df.head())

df = pd.read_csv('biostats.csv', sep='\t')  # For tab-separated files
print(df.head())

df = pd.read_csv('biostats.csv', sep='|')  # For pipe-separated files
print(df.head())

df = pd.read_csv('biostats.csv', header=None)
print(df.head())

df = pd.read_csv('biostats.csv', header=1)  # Use the second row (index 1) as header
print(df.head())

df = pd.read_csv('biostats.csv', nrows=5)
print(df.head())

"""c)Handle missing values and data cleaning.

Handling missing values and performing data cleaning is a crucial part of the data preprocessing process. Pandas provides several methods and techniques to clean and handle missing data effectively.

"""

#Checking for missing values
import pandas as pd

# Sample data with missing values
data = {
    'Name': ['John', 'Jane', 'Jim', None, 'Alice'],
    'Age': [25, 30, None, 35, 28],
    'Salary': [50000, None, 45000, 60000, 55000]
}

df = pd.DataFrame(data)

# Checking for missing values in the entire DataFrame
print(df.isna())

# Check for missing values in a specific column
print(df['Age'].isna())

# Check for missing values in the whole DataFrame (summarized by column)
print(df.isna().sum())


# Remove rows that contain any missing value
df_cleaned = df.dropna()
print(df_cleaned)


# Remove columns with any missing value
df_cleaned = df.dropna(axis=1)
print(df_cleaned)

# Fill missing values with a constant value
df_filled = df.fillna(0)
print(df_filled)


# Fill missing values with the mean of the column (numeric columns only)
numeric_cols = df.select_dtypes(include=['number']).columns
df_filled = df.fillna(df[numeric_cols].mean())
print(df_filled)

"""#10)Python String Methods


Python provides a rich set of string methods that allow you to manipulate and operate on strings efficiently. Below is a detailed overview of some commonly used string methods in Python, with examples for each.

a)Manipulate strings using various built-in methods.

b)Perform operations like concatenation, slicing, finding substrings.

c)Convert strings to uppercase, lowercase, and title case.

d)Remove whitespace and split strings.
"""

#convert the text to uppercase
text = "hello world"
upper_text = text.upper()
print(upper_text)

#convert the text to lowercase
text = "HELLO WORLD"
lower_text = text.lower()
print(lower_text)

#Capitilize the below text
text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)

#Swap the case letters
text = "Hello World"
swapped_case_text = text.swapcase()
print(swapped_case_text)

#White space handling
text = "   hello world   "
stripped_text = text.strip()
print(f"'{stripped_text}'")


#Remove leading white space
text = "   hello world"
lstripped_text = text.lstrip()
print(f"'{lstripped_text}'")


#Remove trailing white space
text = "hello world   "
rstripped_text = text.rstrip()
print(f"'{rstripped_text}'")

#Find the position of substring
text = "hello world"
position = text.find("world")
print(position)


#Check if a String Starts with a Substring
text = "hello world"
starts_with_hello = text.startswith("hello")
print(starts_with_hello)


#Check if a string ends with a substring
text = "hello world"
ends_with_world = text.endswith("world")
print(ends_with_world)


#Replace Substring with Another (replace())
text = "hello world"
replaced_text = text.replace("world", "Python")
print(replaced_text)

#Count Occurrences of Substring (count())
text = "hello world world"
count_world = text.count("world")
print(count_world)


#Split a String into a List (split())
text = "apple,banana,cherry"
split_text = text.split(",")
print(split_text)


#Join a List of Strings into a Single String (join())
words = ['apple', 'banana', 'cherry']
joined_text = ", ".join(words)
print(joined_text)


#Left Justify a String (ljust())
text = "hello"
left_justified = text.ljust(10, '*')
print(left_justified)


#Right Justify a String (rjust())
text = "hello"
right_justified = text.rjust(10, '*')
print(right_justified)


#Center a String (center())
text = "hello"
centered_text = text.center(10, '*')
print(centered_text)


#Zero Padding (zfill())
text = "42"
padded_text = text.zfill(5)
print(padded_text)




#Concatenating strings
# List of words
words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

# Using join to concatenate
sentence = " ".join(words)  # Joining with spaces
print(sentence)

# Another approach using concatenation (slower for large lists)
concatenated_sentence = ""
for word in words:
    concatenated_sentence += word + " "
print(concatenated_sentence.strip())




#Slicing
text = "Hello, Python World!"

# Slicing to extract "Python"
substring = text[7:13]  # From index 7 to index 13 (not including 13)
print(substring)

# Reverse slicing (extract last 6 characters)
last_chars = text[-6:]
print(last_chars)


#Finding substrings
text = "Python is great. Python is fun."

# Find the first occurrence of "Python"
first_pos = text.find("Python")
print(first_pos)

# Find the second occurrence of "Python" (by starting the search after the first occurrence)
second_pos = text.find("Python", first_pos + 1)
print(second_pos)
