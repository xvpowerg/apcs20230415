class BookStack:
    def __init__(self, capacity):
        self.my_stack = [None]*capacity
        self.top = -1
        self.capacity = capacity
    def push(self, data):
        if self.isFull():
            print('書箱已滿!')
        else:
            self.top+=1
            self.my_stack[self.top]=data
    def pop(self):
        if self.isEmpty():
            print('書箱為空!')
            return None
        else:
            data = self.my_stack[self.top]
            self.my_stack[self.top] = None
            self.top-=1
            return data
    def size(self):
        return self.top+1
    def isEmpty(self):
        if(self.top==-1):
            return True
        else:
            return False
    def isFull(self):
        if(self.top>=self.capacity-1):
            return True
        else:
            return False
    def printStack(self):
        for b in self.my_stack:
            print(b, end=',')
        print()
        
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return "%s(%s)" %(self.title, self.author)
    
bookStack = BookStack(3)
books = [Book('鹿鼎記','金庸',500),
         Book('灌籃高手','井上雄彥',750),
         Book('哈利波特','JK 羅琳',800),
         Book('西遊記','吳承恩',450)]

for b in books:
    bookStack.push(b)
    bookStack.printStack()

for i in range(4):
    book = bookStack.pop()
    if book:
        print('取出:', book)
    bookStack.printStack()
