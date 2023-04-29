
def get_sum(a,b):
    return a + b

#get_sum(a,b,c) 會覆蓋get_sum(a,b)
def get_sum(a,b,c):
    return a + b + c

print(get_sum(1,2,3))
print(get_sum(4,5))

