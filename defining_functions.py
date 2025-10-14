def greet():
    print("Hello!")
    print("Welcome aboard")


greet() # calling, invoking, running the function
#the function greet is defferent from print() because it does not take any 

def greet_with_name(name):
    print(f"Hello {name}!")
    print("Welcome ")


greet_with_name("Elain")

#parameter vs argument
#parameter is the input you define in the function
#argument is the actual value for a given parameter 

#Functions can 
# 1 - Preform a specific task

# 2 - Return a value
def get_greeting(name):
    return f"Hello {name}!"

message = get_greeting("Elain")
file = open("greeting.txt", "w")
file.write(message)