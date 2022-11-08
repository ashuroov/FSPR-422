# # HOMEWORK

info = []

for i in range(5):
    name = input('input name')
    age = int(input('input age'))
    info.append(
    {
        'age': age,
        'name': name,
    }
    )
print(info)

result = []
faranheits = [20, 19, 140, 24, 45]
for far in faranheits:
    celsius = (far - 32) * 5 / 9
    if celsius >= 50:
        print('Слишком горячо')
        break
    elif celsius <= 5:
        print('Жить можно')
    result.append(celsius)

print(result)

# ****
# *  *
# *  *
# ****

square_line = 4 
star = "*" 
star_width = star * square_line 
print(star_width) 
print(f"{star}  {star}") 
print(f"{star}  {star}") 
print(star_width) 
for i in range(square_line): 
    print(star, end="")


square_line = 10
star = '*'
star_width = star * square_line
for i in range(square_line):
    if i > 0 and i < (square_line -1):
        empty_space = ' ' * (square_line - 2)
        print(f'{star}{empty_space}{star}')
    else:
        print(star * square_line)


i = 0
while i < 10:
    print('i =', i)
    i += 1
i = 0
while True:
    i += 1
    print('i =', i)
    if i == 100:
        break


names = [1, 2, 3, 4, 5, 6]
i = 0
while i < len(names):
    print(names[i])
    i += 1


s = "ABCDEFG"
for i in range(len(s)):
    s[i]

for i, val in enumerate ("ABCDEFG"):
    print(i, val)


ab = [1, 1, 2, 3, 4, 4, 5, 3]
print(set(ab))



# sort_dict({3:"hello", 2:"hello", 1:"hello"}) == [(1,"hello"), (2,"hello"), (3,"hello")] 
# sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]


def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)
