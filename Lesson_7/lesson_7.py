# Итерируемые - iterable (исчислямые). Это те переменные, которые хранят больше одного значения.
# Индексы

names = [ 1, 2, 3, 4, 5 ]
print(type(names), names[3])
names = ()
print(type(names))

# Dictionary - Словарь
# Ключем словаря может быть только не изменяемые типы переменных.

user_data = {
    'key': 'meaning',
    1: None,
    2: 21,
    3: 6.7,
    4: [2,3,4],
    5: (1,2,3),
    6: {'key': 'Another Dictionary'}
    # [1]: 23 # error
    # (2, 3, [2, 3]): "Not ERROR", # в кортеж можно использовать как ключ, но не рекомендуется
}

# 40-50 ciuyg4kj3hkjb3hvhjkh4r
print(type(user_data), user_data, user_data['key'], sep='\n')

something = {
    'big_key': 'password for key'
}
print(something['big_key'])

user_data = {
    'username': 'Fred',
    'password': 'yeiuwqo1234hfdnsm',
    'age': '27',
}
print(user_data['age'])

user_data_2 = {
    'username': 'Harry',
    'password': 'ye232qo1234hfdnsm',
    'age': '29',
}
print(user_data_2['username'])

user_data_3 = [
    {
        'username': 'John',
        'password': 'ye2329283753fdnsm',
        'age': '99',
    },
    {
        'username': 'Marry',
        'password': 'ye232qo1ooeuhrj4nsm',
        'age': '23',
    },
]

print(user_data_3[1]['age'])


user_data = {
        'username': 'John',
        'password': 'ye2329283753fdnsm',
        'age': '99',
}

user_data['username'] = 'Alabasta'
print(user_data.keys(), user_data.values(), user_data.items(), sep='\n')

# view
# dict_keys(['username', 'password', 'age']) - ['username', 'password', 'age']
# dict_values(['Alabasta', 'ye2329283753fdnsm', '99'])
# dict_items([('username', 'Alabasta'), ('password', 'ye2329283753fdnsm'), ('age', '99')])
# [("username", "Alabasta"), ("password", "ye2329283753fdnsm"), ("age", "99")]

user_list = list(user_data.values())
print(user_list)

print('get', user_data.get("age"), user_data.get("unexisting"))


# set - множество
# нельзя индексировать
# можно менять с помощью методов или циклов

numbers = {2, 3, 4, 'ABCD', 5, 4, 3}
print(numbers)

numbers = {} # выйдет dict - DICTIONARY
print(type(numbers))

numbers = set() # выйдет set
print(type(numbers))

remove_duplicates = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, "AA", "BB", "BB"]
print(remove_duplicates, set(remove_duplicates), sep = "\n")

remove_duplicates = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, "AA", "BB", "BB"]
print(remove_duplicates, list(set(remove_duplicates)), sep = "\n")