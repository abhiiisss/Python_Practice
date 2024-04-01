# Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

Fruit = "Banana"

fruit_Color = input("What color is your banana:")
if Fruit == "Banana":
   if fruit_Color == "Green":
       print("Your Fruit is UNRIPE")
   elif fruit_Color == "Yellow":
        print("Your Fruit is RIPE")
   elif fruit_Color == "Brown":
        print("Your Fruit is OVERRIPE") 
   else:
        print("Your Fruit is not mentioned in the ripped conditions")    
