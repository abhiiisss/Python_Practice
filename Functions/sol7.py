# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def add(*numbers):
    return sum(numbers)

print(add(1,2,3,4,4))  