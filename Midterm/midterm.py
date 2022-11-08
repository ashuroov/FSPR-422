'''
1) PVM это то из за чего работает python и то что делает все операции

2) int - числа
float - числа с остатком
bool - True or False
string - строка

3) Изменяемые - int, float, str
Неизменяемые - dict, list
Их разница в том, что первые можно изменить, а вторые нет))

4) append, remove, insert

5) С помощью in мы можем проверить есть ли это значение в списке и тд. Т.е. если есть то True, если нет то False 
С помощью is мы можем узнать равны ли значения. a = a, b = b

6) LEGB - LOCAL ENCLOSED GLOBAL BUILT-IN / Локальная Встроенная Глобальная 

7) Тут два ответа у меня, либо пусто, либо None
'''
# Примеры для четвертого вопроса
# question_4 = [1, 2, 3, 4]
# question_4.append(6)
# print(question_4)

# question_4 = [1, 2, 3, 4]
# question_4.remove(2)
# print(question_4)

# question_4 = [1, 2, 3, 4]
# question_4.insert(1, 5)
# print(question_4)

"""
ЗАДАЧИ
"""
# Первая задача
ab = [1, 2, 2, 2, 3, 4, 5]
print(ab.count(2))



# Вторая задача

numbers_1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',]
numbers_2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def smth(i):
    if i >= 0 and i < 100:
        return(i) # НЕ СМОГ НАЙТИ И ПРИДУМАТЬ ФОРМУЛУ ДЛЯ ЭТОГО



# Третья задача

a = ["You've got that fire (fire)"]
b = ["The flavor, the style (style)"]
a.append(b)
print(a)



# Четвертая задача

names = [] 
for i in range(9): 
    names.append(i + 4) 
if i == 7: 
    names.pop(0)
print(names) 



# Пятая задача

stroka = ["FREDDY", "KTO-TO", "JOHN"] 
slovo = 'JOHN' 
count = stroka.count(slovo) 
if count > 0: 
    print(slovo)
else:
    print(-1)



# Шестая задача

creations = {
    "race": "alien",
    "age": "928"
}

if creations == int or str:
    print(creations.get())
else:
    print("HUMAN")
