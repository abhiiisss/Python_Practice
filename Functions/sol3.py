# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.


# p1 = input("First input: ")
# p2 = input("Second input: ")

def multiply(p1, p2):
    return p1 * p2

print("Your output is:", multiply(5, 5))
print("Your output is:", multiply("A", 5))
print("Your output is:", multiply(5, "S"))
