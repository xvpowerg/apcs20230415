values = input("Input Number:")
newStrList =values.split()
intList = list(map(int,newStrList))
#intList = list(map(int,input("Input Number:").split()))
print(intList)
print(type(newStrList[0]))
print(type(intList[0]))

