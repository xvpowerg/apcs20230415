class Employee:
    compnay = "IBM"
    def __init__(self,name,salary=20000):
        self.name = name
        self.salary = salary
    def printInfo(slef):
        print("Name:",slef.name)
        print("Salary:",slef.salary)
        print("Compnay:",Employee.compnay)
        
emp1 = Employee("Sean",50000)
emp2 = Employee("Ken",70000)

emp1.printInfo()
emp2.printInfo()
Employee.compnay = "FB"
emp1.printInfo()
emp2.printInfo()

