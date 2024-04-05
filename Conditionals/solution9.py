# Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# #Usual way to find leap year
# Leap_year_checker = int(input("Which Year is it:"))

# if Leap_year_checker % 2 == 0:
#     year = "This is a leap year"
# else:
#     year = "This is a normal year"  

# print(year)

#finding leap year using conditions 

year = int(input("What year is it:"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    year_checker = f"{year} is a leap year"

else:
    year_checker = f"{year} is a not a leap year"

print(year_checker)