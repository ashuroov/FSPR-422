numbers = (1, 2, 3, 4, 5, 6, 7)
for num in numbers:
    print(num * 4)



numbers = [1, 2, 'Abdulaziz', 4, 5, 6, 7]
numbers[2] = 3
for num in numbers:
    print(num * 4)

for val in [1, 2, 3, 4, 5, [6, 7, 8, 5, 6], (4, 5, 6)]: 
    print(val) 
    if isinstance(val, (list, set, tuple)): 
        for i in val: 
            print(i)

# Не получилось

