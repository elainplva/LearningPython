number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# infinite loop
while True:
    command = input(">")
    if command.lower() == "quit":
        break # exit loop
    print("ECHO", command)