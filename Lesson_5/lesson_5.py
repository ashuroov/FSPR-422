'''
НЕИЗМЕНЯЕМЫЕ
int
float 
str
bool
None 
frozenset - множество замороженное
tuple - кортеж
bin
 

ИЗМЕНЯЕМЫЕ
list - список
dict - словарь
set - множество


Прочитать про:
    complex
    Decimal
    Fraction
'''

# #012345
# 'sdrftd'

# names = []
# print(names)

# names = list()
# print(names)

# #        0  1  2  3  4  5    6      7      8     9
# names = [1, 2, 3, 4, 5, 6, 12.5, 'ABCD', True, None]
# print(names)
# names[0] = False
# print(names)

# #names[7] = 'Name
# print(names[7] [0]) #ABCD -> A


# names = [[2, 3, 4], [4.5, 5.5, 6.6], ['go', 'go1', 'go2']]
# print(names[2][2])

# Нарезка - Slice
# итерировать - проходиться по элементам итерируемых переменных (это такие переменные, которые могут хранить больше одного значения)

#          0  1  2   3   4   5   6
numbers = [4, 5, 6, 10, 22, 55, 500]
#          -7 -6 -5 -4  -3  -2   -1

# [начало:конец]
print(numbers[1:4]) # индекс не включительный
print(numbers[:], numbers)
print(numbers[1:])
print(numbers[:5])

#начало:конец:шаг
print('шаг', numbers[:6:2]) # 0 + 2 -> 2 + 2 -> 4 -> 6
print('шаг', numbers[:], numbers)
print('шаг', numbers[::2]) # 0 + 2 -> 2 + 2 -> 4 + 2 -> 6
print('шаг', numbers[::10]) # 0 + 10

print(numbers[-1])