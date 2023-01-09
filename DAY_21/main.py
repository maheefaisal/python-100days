'''Day 21 of python

'''
#default arguments for a function
'''def average(a=1,b=2):
    print((a+b)/2)

average()

'''

#arbitary arguments

def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)



c= average(1,2,4,5)

print(c)
