x = [5, 15, 25, 35, 45]

for v in x:
    print(v,end=" ")
print()    
x.insert(1,200)

x.append(100)

x[2] = 20

print(x)

x.remove(20)
print(x)
n = x.pop()
print(n)
print(x)
n = x.pop(2)
print(n)
print(x)
