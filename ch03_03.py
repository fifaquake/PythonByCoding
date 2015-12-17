a = {}
b = {2: 'sea', 3: 'River', 8: 'Mountain'}
c = {2: {4: 'abcd', 5: 'hjkl'}, 3: 'vbnm'}
d = dict(name = 'elena', age = 30, roles =('manager', 'consultant'))

print(a)
print(b)
print(c)
print(d)

print(b.keys())
print(b.values())
print(b.items())

a.setdefault(2, 'car')
a.setdefault(5, 'train')
a.setdefault(7, 'plane')
print(a)

print(3 in b)
print(5 in b)