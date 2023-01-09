'''Day 38 of python'''

'''Example One (1)'''
'''
# define Python user-defined exceptions
class InvalidAgeException(Exception):
 
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Voter Invalid Age")
'''

'''Example Two(2)'''
a = int(input('Enter a value: '))

if(a>5):
    raise VlaueError("Value should be less than 5")




















