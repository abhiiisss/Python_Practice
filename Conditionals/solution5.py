# Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

Weather = input("What is Today's Wheather:")

if Weather == "Sunny":
    activity =  "Go for a Walk"
elif Weather == "Rainy":
    activity =  "Read a Book"
elif Weather == "Snowy":
    activity =  "Build a Snowman"   

print(activity)        