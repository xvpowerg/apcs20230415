a1,a2 = 1,3
print(a1,a2,sep=" ",end=" ")

for i in range(3,8):
    a3 = 3*a2 - 2*a1
    print(a3,end=" ")
    a1 = a2
    a2 = a3
print()

def senFunc(x):
    if x == 1:
        return 1
    elif x == 2:
        return 3
    else:
        return 3 * senFunc(x-1) - 2 * senFunc(x-2)
for j in range(1,8):
    print(senFunc(j),end=" ")
    
