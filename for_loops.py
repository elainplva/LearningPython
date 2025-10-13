for number in range(3):
    print("Attempt", number + 1)

for number in range(4):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):
    print("Attempt", number, number * ".")

for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

#For loops with else
successful = False
for number in range(3):
    print("Attempt", number + 1)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

#Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

#Iterables
for x in range(5):
    print(x)

for y in "Python":
    print(y)

for z in [1, 2, 3, 4]:
    print(z)

    