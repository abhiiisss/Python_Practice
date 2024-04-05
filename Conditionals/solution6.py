# Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

Distance = int(input("How far it is:",))

if Distance < 3:
    transportation = "Walk"
elif Distance <= 15:
    transportation = "Bike"
else:
    transportation = "Car"        

print("you should take a",transportation)    