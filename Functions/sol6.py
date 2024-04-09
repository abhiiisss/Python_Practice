# 6. Lambda Function
# Problem: Create a lambda function to compute the cube of a number.

x = int(input("Give a number to get his cube: "))

cube = lambda x: x ** 3

print("The cube of given number is:",cube(x))