print('-----declare list')
numbers = []
a = [2, 7, 10, 8]
cities = ['Berlin', 'Seattle', 'Tokyo', 'Moscow']
b = [10, 3, 'Apple', 6, 'Strawberry']
c = range(1, 10, 2)

print('----print(lists)')
print(a)
for city in cities:
    print(city)

print(b)
print(c)

print('-----get length of lists')
print(len(a))
print(len(cities))

print('-----add items')
numbers.append(10)
numbers.append(5)

cities.append('London')
for i in numbers:
    print(i)

for city in cities:
    print(city)

print('-----get item')
print(cities[2])
print(a[3])
print(a.sort())
for b in a:
    print(b)

print('-----edit item')
cities[2] = 'new city'
for city in cities:
    print(city)

print('-----remove item')
a.remove(8)  # by value
del cities[2]  # by index
for city in cities:
    print(city)
