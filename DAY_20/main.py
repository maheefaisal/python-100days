'''Day 20 of python
Function
'''
def calculategmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def calculategreaternumber(a,b):
    if(a>b):
        print("a is greater than b")
    else:
        print("b is greater than a")
a=5
b=5
calculategmean(a,b)
calculategreaternumber(a,b)

d=55
v=54
calculategmean(d,v)
calculategreaternumber(d,v)
