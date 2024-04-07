# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

n = int(input("number:"))
factorial = 1

while n > 0:
    factorial *= n
    n -= 1

print("The factorial of your given number is:", factorial)