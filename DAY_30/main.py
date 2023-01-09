'''Day 29 of python'''
'''Recursion  in python'''
#factorial
'''
def factorial(n):
    if(n==0 or n==1):
        return 1

    else:
        return n * factorial(n-1)

print(factorial(3))
'''

#fibonacci

def fibo(n):

    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

print(fibo(6))
