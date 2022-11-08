# is и =

a = (1, 2, 3)
b = (1, 2, 3)
print(a is b, a == b)

b = [2, 3, 4]
b.append(23) # [2, 3, 23]
a = [2, 3, 4]
print(a is b, a == b)

# a это b/b это a

a = [2, 3, 4]
b = a 
b.append(43)
print('a=', a, 'b=', b)

# с копированием
a = [2, 3, 4]
b =a.copy()
b.append(43)
print('a=', a, 'b=', b)

# с копированием
a = [2, 3, 4, [2, 3]]
b =a.copy()
b[2] = 400
b[3][1] = 12
print('a=', a, 'b=', b)

# Модуль для глубокого копирования
import copy

a = [2, 3, 4, [2, 3]]
b = copy.deepcopy(a)
b[2] = 400
b[3][1] = 12
print('a=', a, 'b=', b)



# isistance('qwerty', (int, str)) # True

# isistance('qwerty', (int, str))

print(type('qwerty'), str, 'qwerty' == str)

val = ['12']
if type(val) == int or type(val) == str:
    print(True)
else:
    print(False)

print('list')
numbers = [1, 2, 3, 4, 5, 6, 7]
for num in numbers:
    print(num + 3)

print('tuple')
numbers = (1, 2, 3, 4, 5, 6, 7)
for num in numbers:
    print(num + 3)

print('set')
numbers = {1, 2, 3, 4, 5, 6, 7}
for num in numbers:
    print(num + 3)

print('dict')
user = {
    'name': 'Abdulaziz',
    'age': '20',
    'skill': 'POQW',
}
for key in user:
    print(key)


print('dict vals')
for val in user.values():
    print(val)

print('\ndict items')
for key, val in user.items():
    print('key =', key, 'val=', val)




for val in [1, 2, 3, 4, 5, [6, 7, 8]]:
    print(val)
    if isinstance(val, (list, set, tuple)):
        for i in val:
            print(i)
            