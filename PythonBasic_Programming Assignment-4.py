# 1. Write a Python program to find factorial of a number.

def get_factorial():

    n = int(input("Enter the number: "))
    a = 1

    if n == 0:
        print("Factorial of 0 is 1.")

    elif n < 0:
        print("No factorial exists for negative numbers.")

    else:
        for i in range(1,n+1):
            a = a * i
        print(f"The factorial of {n} is {a}.")


# 2. Write a Python Program to Display the multiplication Table?

def multiplication_table(number):
    for i in range(1,11):
        sol = number * i
        print(f"{number}*{i} = {sol}")


# 3. Write a Python Program to Print the Fibonacci sequence?
def fibonacci_sequence(n):
    # First two terms of a Fibonacci sequence
    n1, n2 = 0, 1
    counter = 0

    if n < 0:
        print(f"{n} must be positive.")

    elif n==1:
        print(f"Fibonacci sequence up to {n} is {n1}")

    else:
        print("Fibonacci sequence is: ")
        while counter < n:
            print(n1)
            x = n1 + n2
            n1 = n2
            n2 = x
            counter += 1


# 4. Write a Python program to check Armstrong number.
def armstrong_number_check():

    num = int(input("Enter a number: "))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")


# 5. Write a Python program to check Armstrong number in an interval.

def armstrong_number_interval(lower_limit, upper_limit):

    for num in range(lower_limit, upper_limit + 1):

        order = len(str(num))
        sum = 0

        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print(num)


# 6. Write a Python Program to Find the Sum of Natural Numbers?
def sum_of_natural_numbers():
    num= int("Enter a positive number: ")

    if num <= 0:
        print("Please enter a valid natural number")

    else:
        sum= 0
        while num > 0:
            sum += num
            num -= 1

        print(f"Sum is {sum}")










