class Node():
   def __init__(self,data = None):
       self.data = data
       self.next = None
n1 = Node(5)
n2 = Node(15)
n3 = Node(25)

class Linked_list():
    def __init__(self):
        self.head = None
    def print_list(self):    
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
    def add_front(self,item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
    def add(self,item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = newNode
    def getNode(self,index):
         ptr = self.head
         for i in range(index):
             ptr = ptr.next
             if ptr == None:
                 break
         return ptr       
             
link = Linked_list()
data = [5,15,25]
for n in data:
    link.add(n)
link.print_list()
node = link.getNode(2)
print(node.data)
