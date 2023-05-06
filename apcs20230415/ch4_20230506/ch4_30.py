list1 = ['a','b','c']
print(list1)

list1.append("d")
list1.append("e")
print(list1)
list1.append(["f","g"])
print(list1)
# extend 才會展開到list
list1.extend(["h","i"])
print(list1)

