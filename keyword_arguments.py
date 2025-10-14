def increment(number, by):
    return number + by


print(increment(2, by=1)) # keyword argument

#Keyword arguments are often used when a function has many parameters, 
# and you want to be clear about which value goes to which parameter.

#Defaault Arguments
def increment(number, by=1):
    return number + by

print(increment(2, 5)) # if by is not provided, it will use the default value of 1