# Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("Which size would you prefer your Coffee:")

extra_shot = input("Do you want any extra shot:")

if extra_shot == "Yes":
    coffee = order_size + " Coffee with an extra short"
elif extra_shot == "No":
    coffee = f"Your {order_size} coffee is ready"
else: 
    coffee = "Your Coffee is not available"

print("Your Order:",coffee)    
