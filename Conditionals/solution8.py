# Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Password:")


if len(password) < 6:
    password_strength = "Weak Password"
elif len(password) <= 10:
    password_strength = "Medium Password"
else:
    password_strength = "Strong Password"

print("Password strength is:",password_strength)
