class Employee:
    def __init__(self,name,salary=20000):
        self.name = name
        self.salary = salary
    def printInfo(slef):
        print("Name:",slef.name)
        print("Salary:",slef.salary)
        
emp1 = Employee("Sean",50000)
emp2 = Employee("Ken",70000)
'''
print(emp1.name)
print(emp1.salary)

print(emp2.name)
print(emp2.salary)
'''
emp1.printInfo()
emp2.printInfo()
