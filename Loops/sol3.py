# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

n = 10

for i in range(1, n+1):
    if i == 5:
        continue
    print(n, "x", i, "=", n * i)