def personInfo(name,age,**other):
    print("=============")
    print("name:",name)
    print("age:",age)
    for key in other:
        print(key,":"+other[key])

personInfo("Sean",40)
personInfo("David",35,phone="8825522",compnay= "IBM")
