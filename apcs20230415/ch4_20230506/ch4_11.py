def func(thelist):
        print("func():",id(thelist),thelist)
        thelist[2] = 'Hi'
        print("func():",id(thelist),thelist)
mylist = [10,20,30]

print("mylist:",id(mylist),mylist)
func(mylist)
print("mylist:",id(mylist),mylist)
