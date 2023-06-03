'''for i in range(1,6):
    for k in range(5-i):
        print(" ",end="")
    for i in range(i):
        print("*",end="")
    print("")
'''
for i in range(1,6):
    print(" "*(5-i),"*"*i,sep="")

