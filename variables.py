# using triple quotes for multi line strings

message = '''
Hi John,
Here is our first email to you.
Thank you,  
The support team
'''
#len() # function to get length of string

print(len(message))

students_count = 1000
rating = 4.99
is_published = True # bullon values
course = " Python Programming"
print(course[0]) # first character
print(course[-1]) # last character
print(course[0:3]) # slicing

sentence = "Python \"Programming" # escape sequence
print(sentence)
#/n for new line
#/t for tab

first = "John"
last = "Smith"
full = f"{first} {last}" # formatted string
print(full)
print(course.upper())
print(course.title())
print(course.strip()) # removes white space

