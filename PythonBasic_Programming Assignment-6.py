import math
# 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?

def fibonacci_seq_recursion(n):

    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 0:
        return 0
        # Second Fibonacci number is 1
    elif n == 1:
        return 1
    else:
        return fibonacci_seq_recursion(n - 1) + fibonacci_seq_recursion(n - 2)


# 2. Write a Python Program to Find Factorial of Number Using Recursion?

def factorial_using_recursion(x):

    if x == 1:
        return 1
    else:
        return x * factorial_using_recursion(x-1)


# 3. Write a Python Program to calculate your Body Mass Index?

def bmi_calculator():
    height= float(input('Enter height (in m): '))
    weight= float(input("Enter weight (in kg): "))

    bmi= height/(weight**2)

    print(f"BMI is {bmi}")

# 4. Write a Python Program to calculate the natural logarithm of any number?

def natural_Log(x):
    print(math.log(x))



# 5. Write a Python Program for cube sum of first n natural numbers?

def cube_sum():
    n= int(input("Enter natural number: "))

    if n <= 0:
        print("Enter a natural number")

    else:
        n1 = n
        sum_of_cubes = 0

        while n1 > 0:
            temp= n1**3
            sum_of_cubes += temp
            n1-=1

        print(f"Cube sum of first {n} numbers is {sum_of_cubes}")
