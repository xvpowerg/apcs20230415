class item:    
    def __init__(self,weight,value):
        self.weight = weight
        self.value = value
        self.unitValue = self.value / self.weight
    def __lt__(self,other):
       return self.unitValue < other.unitValue
    def __str__(self):
        return f"({self.weight}:{self.value})"
class Knapsack:
    def __init__(self,capcity):
        self.capcity = capcity
        self.items = []
        self.weight = 0
        self.value = 0
    def put(self,item):
        if self.weight + item.weight > self.capcity:
            return False
        else:
            self.items.append(item)            
            self.weight += item.weight
            self.value += item.value
            return True
    def print(self):
        for item in self.items:
             print(item)
             
weights = [1,2,3]
values = [20,60,45]
capcity = 5
k =  Knapsack(capcity)
items = []
for w,v in zip(weights,values):
    items.append(item(w,v))
sortItems = sorted(items,reverse = True)
for i in sortItems:
    if not k.put(i):
        break
k.print()

""" 
i1 = item(2,60)
i3 = item(1,20)
i2 = item(3,45)


k =  Knapsack(5)
print(k.put(i1))
print(k.put(i2))
print(k.put(i3))
k.print()
"""
