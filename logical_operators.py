high_income = True
good_credit = True
student = False
 
 #Short circuit evaluation
if high_income and good_credit: #and operator
    print("Eligible for loan")
else:
    print("Not eligible for loan")

if high_income or good_credit: #or operator
    print("Eligible for loan")
else:
    print("Not eligible for loan")

if not student:               #not operator
    print("Eligible for loan")
else:
    print("Not eligible for loan")


if (high_income or good_credit) and not student: #parentheses to clarify that at least one of the starements is true
    print("Eligible for loan")
else:
    print("Not eligible for loan")

#Chaining comparison operators
# age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("Eligible")