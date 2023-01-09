'''Day 15 of 100 days of python'''

#importing time module
import time

'''
sec = time.time()
print(sec)
'''
'''Time module imported and use'''
local_time = time.localtime(sec)

'''Time module for hour'''
print(local_time.tm_hour)


'''If conditions for the greetings'''

if(local_time.tm_hour>0 and local_time.tm_hour<12):
    print("Good morning")
    
if(local_time.tm_hour>12 and local_time.tm_hour<17):
    print("Good Afternoon")

if(local_time.tm_hour>=18 and local_time.tm_hour<22):
    print("Good Evening")

else:
    print("Good Night")
