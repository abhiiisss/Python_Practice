# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

user_input = input("Give us a str to find 1st non-repeated charachter:")

for i in user_input:
    print(i)
    if user_input.count(i) == 1:
        print("The non-repeated character is:", i)
        break