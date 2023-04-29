subjs = ['國語','數學','英文']
scores = [100,80,95]

for i in range(len(subjs)):
    print(subjs[i],scores[i])

print(list(zip(subjs,scores)))

for n,s in zip(subjs,scores):
    print(n,s)


print("======================")
# 使用過一次不能再用
myZip = zip(subjs,scores)

#print(list(myZip))

for n,s in myZip:
    print(n,s)
print("======================")
for n,s in zip(subjs,scores):
    print(n,s)    


