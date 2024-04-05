# Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = input("What type of pet you have:")
age = int(input("what is your pet's age:"))

if (pet == "Dog") and (age <= 2):
    pet_food = "Puppy food"
elif (pet == "Cat") and (age >= 5):
    pet_food = "Senior Cat food"
else:
    pet_food = "Recommendation failed"    

print(pet_food)