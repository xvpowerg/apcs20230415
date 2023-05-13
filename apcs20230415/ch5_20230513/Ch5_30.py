class Employee:
    compnay = "IBM"
    count = 0
    def __init__(self,name,salary=20000):
        self.name = name
        self.salary = salary
        Employee.count += 1
    def printInfo(slef):
        print("Name:",slef.name)
        print("Salary:",slef.salary)
        print("Compnay:",Employee.compnay)
    def getTotal():
        return Employee.count
emp1 = Employee("Sean",50000)
emp2 = Employee("Ken",70000)
emp3 = Employee("Vivin",20000)
emp1.printInfo()
emp2.printInfo()
emp3.printInfo()
print(Employee.getTotal())

