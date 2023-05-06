a = 5

def func():
    global a 
    a +=  2
    print("func(): a =",a)
    
print("a= ",a)
func()
print("a= ",a)
