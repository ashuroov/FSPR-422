# Матрица
# [2,3,4,5,6] # вектор
matrix = [[2,3,4], [5,6,7]] # матрица 3 столбца и 2 строки
print( matrix[1][1])

# random = list(1) # error
# random = list(True) # error
random = list('Random')
splitted_string = 'Split me!'.split(' ') # ' ' из за пробела между SPLIT и ME он делит на две строки
print(random, splitted_string)

splitted_string = 'Split me!'.split(' ') 
print(random, splitted_string, ''.join(random), sep='\n')

# # Tuple - кортеж итерабл/iterable

numbers = (2, 3, 4, 5, 6)
print(numbers, numbers[3])

numbers = ((4, 5), 4.5, 'abcd', [5, 6, 7])
print(numbers, numbers[3])

# # numbers[1] = 'Changed'
# # Tuple можно читать и создавать

numbers = (2, 3, 4, [6, 7])
numbers[3][0] = 24
print(numbers[3], numbers[3][0])


numbers = [[2, 3, 4], [5, 6], 7, 8, 9]
print(numbers[0][2])


numbers = (2, 3, 4)
print('1', type(numbers), numbers)
numbers = tuple()
print(type(numbers), numbers)
numbers = ()
print(type(numbers), numbers)
numbers = 2, 3, 4
print(type(numbers), numbers)