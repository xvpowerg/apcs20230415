a = 'Hello'
b = 'World'

print(b is a)
print(b is not a)

print(id(b))
print(id(a))

b = 'Hello'
print(b is a)
print(b is not a)

print(id(a))
print(id(b))
