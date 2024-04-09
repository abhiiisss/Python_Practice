# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

n = int(input("Give the number to get his factorial: "))

def factorial(n):
    if n == 0:
        return 1
    else:    
        return n * factorial(n - 1)

print("The Factorial is:",factorial(n))