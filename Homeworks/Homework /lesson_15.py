n = 15
def factorial(n): 
    if(n == 1 or n == 0): 
        return 1 
    else: 
        return n*factorial(n-1) 

print('The Factorial of', n, 'is:', factorial(n))


