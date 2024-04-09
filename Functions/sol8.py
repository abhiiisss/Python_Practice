# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def keyword(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

keyword(
    name = "Abhishek",
    Age =  22
)

keyword(
    name = "Abhishek",
    Age =  22,
    position = "Data Scientist"
)

