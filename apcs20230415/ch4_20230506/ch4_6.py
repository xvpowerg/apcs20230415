def f1(x,y,*z):
    print(x,y,z)
def f2(x,y,**z):
    print(x,y,z)
f1(1,2,3,4,5,6)
f2(1,2,k1=3,k2=4)
f2(1,k1=3,k2=4,y=8)

