a = 5

def func():
    #因為a是外部變數 無法呼叫 a = a + 2
    a +=  2
    print("func(): a =",a)
    
print("a= ",a)
func()
print("a= ",a)
