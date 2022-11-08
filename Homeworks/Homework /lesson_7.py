x = {'fly', 'go', 'trust'}
y = {"help", 'run', 'fly'}
print(x.union(y))


house = {
    'name': 'Private House',
    'built': '1982',
    'floors': '3',
}

house.update({'pool': 'winter-pool'})
print(house)


numbers = {1, 3, 4, 87}
numbers.add(8)
print(numbers)


shot = {'fly', 'go', 'trust'}

shot.pop()
print(shot)


colors = {'white', 'blue', 'yellow', 'green'}
colors.remove('blue')
print(colors)


house = {
    'name': 'Private House',
    'built': '1982',
    'floors': '3',
}

house.clear()
print(house)


words = {'qwerty', 'labor', 'pollutions'}
words_1 = {'qwerty', 'pop', 'pollutions'}

print(words.difference(words_1))

print(words_1.difference(words))

