# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.


n = int(input("Give me a number:"))
sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += i #here in this code the sum_even gets addedd to each iterable which gives us the main output

print("The sum of even", n, "is:",sum_even)