str1 = "hello world"
str2 = "python"

print(str1 + " " + str2)
print(str1, str2)
print("%s %s" % (str1, str2))
print("{} {}".format(str1, str2))

a = "2"
b = "6.8"

num1 = int(a)
num2 = float(b)

a = 6
b = 8.56

str1 = str(a)
str2 = str(b)
print(str1)
print(str2)

#parsing
msg = 'Berlin;Amsterdam;London;Toyko'
cities = msg.split(';')
for city in cities:
    print(city)

#string operation
msg = 'Hello world, Python!'
print(msg.upper())
print(msg.lower())

print(msg[5:])
print(msg[:5])
print(msg[-3:])
print(msg[:-3])
print(msg[2:6])
print(msg[5:8])

length = len(msg)
print(length)