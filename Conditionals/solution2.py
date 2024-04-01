# Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
persons_age = int(input("what is your age:"))
day = "Wednesday"

price = 12 if persons_age >= 18 else 8

if day == "Wednesday":
    price -= 2 # price = price - 2
else:
    price = price
 
print("Your Movie Ticket Price is $",price)

   

