"""
LEGB - Local Enclosed Global Built-in    -    Локальный Вложенный Глобальный Встроенный
"""



print(print) # builtin

# Любой объект
name = 'Abdulaziz' # global

def get_name():
    name = "Richard" # local
    print(name)


get_name()


name = "Dave"

def spam():
    # LOCAL
    name = "Guido"

spam()
print(name)

# MODIFYING GLOBAL variables

name = "Dave"

def spam():
    global name # imports a global 
    name = "Guido"

spam()
print(name)

# ARGUMENT PASSING 
# при передаче данных к функциям из реальных переменных, значения меняются

def foo(items):
    items.append(42)    # MODIFIES THE INPUT OBJECT

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
foo(a)
print(a)

# REASSIGNMENT VS MODIFYING
# есть разница между пересозданием объекта и изменения его значения

def foo(items):
    items.append(42)   # изменет значение списка

a = [1, 2, 3]
foo(a)
print(a)    # [1, 2, 3, 42]

# VS

def bar(items):
    items = [4, 5, 6]

b = [1, 2, 3]
bar(b)
print('b не изменялось', b)     # [1, 2, 3]


def parent():
    a = 5
    return a 

print("не вложенный", parent())    # 5


# LOCAL ENCLOSED GLOBAL BUILT-IN

def parent():
    a = 5
    def answer():
        return a
    return answer()

print("вложенный", parent())       # 5


# LOCAL ENCLOSED GLOBAL BUILT-IN
# GLOBAL

a = 20 
def parents():
    # ENCLOSED
    a = 5
    def answer():
        a = 10
        def get():
            return a
        return get()
    return answer()

print("вложенный", parents())

# NONLOCAL VARIABLE

def outer():
    # ENCLOSED
    x = "local"

    def inner():
        # LOCAL
        nonlocal x
        x = "non local"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()


# РЕКУРСИВНАЯ ФУНКЦИЯ - ЭТО ФУНКЦИЯ КОТОРАЯ ВОЗВРАЩАЕТ САМОГО СЕБЯ

# def recursion(n):
   # print("РЕКУРСИЯ", n)
   # return recursion(n + 1)

# recursion(0)