class Queue():
    ''' Queue佇列 '''
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity        
    def isEmpty(self):
        ''' 佇列是否為空 '''
        return len(self.queue)==0
    def isFull(self):
        ''' 佇列是否已滿 '''
        return len(self.queue)==self.capacity
    def enqueue(self, data):
        ''' data加入佇列 '''
        if(self.isFull()):
            print("佇列已滿!")
            return 
        self.queue.append(data)
    def dequeue(self):
        ''' 佇列取出data '''
        if(self.isEmpty()):
            print("佇列為空!")
            return None
        return self.queue.pop(0)    
    def size(self):
        ''' 回傳佇列長度 '''
        return len(self.queue)

queue = Queue(3)
people = ['Amy', 'David', 'Sean', 'Nicole']
for person in people:
    print('將 %s 排入佇列' %person)
    queue.enqueue(person)
print('佇列中有%d個人' %queue.size())

for i in range(4):
    item = queue.dequeue()
    if(item):
        print('佇列中取出%s' %item)
print('佇列中有%d個人' %queue.size())
