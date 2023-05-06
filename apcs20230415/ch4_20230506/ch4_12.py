def func(thelist):
        print("func():",id(thelist),thelist)
        thelist = [7,8,9]
        print("func():",id(thelist),thelist)
mylist = [10,20,30]

print("mylist:",id(mylist),mylist)
func(mylist)
print("mylist:",id(mylist),mylist)
