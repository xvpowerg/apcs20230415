greet = "Hi,ed"
print(id(greet),":",greet)
#greet[3] = "E"
newStr = greet.replace("e","E")
print(id(greet),":",greet)
print(id(newStr),":",newStr)
