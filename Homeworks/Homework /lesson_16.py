
# Fibonacci

def fibonacci(i):
    if i in (1, 2):
        return 1
    else:
        return fibonacci(i - 1) + fibonacci(i - 2)
    

print(fibonacci(12))

# [(4, True), (5, False), (3, True)]) -> [6, 30, 125] 
i = 0 
while i < 4 + 1: # 6 
    i += 1 
    j = 0 # 5 
    while j < 5: # 5 
        j += 1 
        z = 0 # 4 
        while z < 3: # 4 
            z += 1 
            pass # 3 
 
        