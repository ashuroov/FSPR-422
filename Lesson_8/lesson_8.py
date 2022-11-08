# bool
# True | False
# любле число что не ноль - это правда (TRUE)
# если переменная пустая - то она ложь (FALSE)

# True = 1      False = 0 

# print(False * 3)

x = 15
y = 25
if x > y:
    print(True)
else: 
    print(False)

'name surname'.split() # ['name', 'surname']
# a if condition else b
print(True if x > y else False)

if []: # True
    print(True)

if -19: # True
    print(True)

name = 'Abdulaziz'
age = '20'
surname = 'Ashurov'

if name == 'Abdulaziz' and age == '20':
    print(name, age)
else:
    print('AND')

if name == 'Abdulaziz' or age == '12':
    print(name, age)
else: 
    print('OR')

if not name:
    print(name)
else:
    print("Name is False")

#                       True                        True 
#       True                  True                
if (name == "Abdulaziz" and age >= '20') or surname == 'Ashurov':
    print(name, age, surname)
else: 
    print('Invalid name, surname, age')

if name == 'Abdulaziz' or age >= "20" and surname == 'Ashurov':
    print(name, age, surname, 'second output')
else:
    print('Invalid name, age, surname')     


# is, ==
# is - сравнивает id двух значений
# id()

a = 1
b = 1
print( id(a), id(b) )

print( id((1, 3)), id((1, 2)) )

print( '1 == 1', 1 == 1, 1 is 1)


t_1 = [] 
t_2 = []
print( id(t_1), id(t_2) )

k_1 = ([])
k_2 = ([])
print( id(k_1), id(k_2) )

l_1 = ()
l_2 = ()
print( l_1 == l_2 )
print( 'tuple', l_1 is l_2 )

# Изменяемые типы данных 
# [] []
p_1 = [1, 2]
p_2 = [1, 2]
print(p_1 == p_2)
print(p_1 is p_2)

g_1 = {1: 1}
g_2 = {1: 1}
print('dict', g_1 == g_2 )
print('dict2', g_1 is g_2)

isinstance

name = 12
print(isinstance(name, str))
print(isinstance(name, (str, int)))

argument = input('Введите что-то;').split()