def calc(x,y):
    z = x **2 + y ** 2
    print(f"(x,y,z)=({x},{y},{z})")
    return z

a,b = 3,4
c = calc(a,b)
print(f"(a,b,c)=({a},{b},{c})")
# x只能在calc內存取
print(f"x:",x)
