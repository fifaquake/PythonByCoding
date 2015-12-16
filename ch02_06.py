a = 3
b = 8
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print((a == b)and (a != b))
print((a <= b) or (a > b))
print(not(a >= b))

m = 0b01010011
n = 0b11111001

print(m)
print(n)
print(bin(m & n))
print(bin(m | n))
print(bin(m ^ n))
print(bin(~m))
print(bin(m << 3))
print(bin(m >> 2))