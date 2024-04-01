#Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

user_age = int(input("What is your age:"))

if user_age < 13:
    print("You are a Child")
elif user_age < 20:
    print("You are a Teenager")
elif user_age < 60:
    print("You are an Adult")
else:
    print("You are Old")
       