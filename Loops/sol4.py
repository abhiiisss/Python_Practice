# 4. Reverse a String
# Problem: Reverse a string using a loop.

user_input = input("Give us a string:")

reversed_Str = " "

for i in user_input:
    reversed_Str = i + reversed_Str

print("Your reversed string is:", reversed_Str)