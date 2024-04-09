# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.



def greet(user = "New_User" ):
    if user != "":
       return  user + ", How you doin?"
    else:
        return "New_User, How you doin?"
    ser
user = input("what is your name: ")
print(greet(user))    


#here default parameter was working pefectly fine untill i was not taking any user input as soon as i started taking the user input i am getting few errors that's why i have used an if-else statement to use a default name while greeting.
