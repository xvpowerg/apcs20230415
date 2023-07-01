class PolyNode:
    def __init__(self, coeff=0, power=0, nxt=None):
        self.coeff = coeff
        self.power = power
        self.next = nxt
    def __str__(self):
        return str(self.coeff) + 'x^' + str(self.power)
# 建立多項式的鏈    
class PolyLL:
    def __init__(self, expression=[]):
        self.head = None
        for element in expression:
            if self.head == None:
                self.head = PolyNode(element[0], element[1])#element[0] 係數 element[1] 指數
            else:
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                if temp.next == None:
                    temp.next = PolyNode(element[0], element[1]) #放到最後的節點
    def show_poly(self):
        temp = self.head
        while temp.next != None:
            print(temp, end = ' + ')
            temp = temp.next
            if temp.next == None:
                print(temp, end=' = 0\n')#最後項次不要加上＋

    def add(self, poly2):
        result = PolyLL()
        result.head = PolyNode()
        ptr = result.head#c(x)
        ptr1 = self.head#a(x)
        ptr2 = poly2.head#b(x)
        while ptr1 or ptr2:#ptr1 or ptr2 有內容時
            if not ptr2: #ptr2是空的 將ptr1放到ptr
                ptr.next = PolyNode(ptr1.coeff, ptr1.power)#將ptr1放到ptr
                ptr1 = ptr1.next
                ptr = ptr.next
            elif not ptr1:#ptr1是空的 將ptr2放到ptr
                ptr.next = PolyNode(ptr2.coeff, ptr2.power)#將ptr2放到ptr
                ptr2 = ptr2.next
                ptr = ptr.next
            elif ptr1.power > ptr2.power:#ptr1大於ptr2 將ptr1放到ptr
                ptr.next = PolyNode(ptr1.coeff, ptr1.power)#ptr1放到ptr
                ptr1 = ptr1.next #將ptr1往下一筆
                ptr = ptr.next #將ptr往下一筆
            elif ptr1.power < ptr2.power:#ptr2大於ptr1 將ptr2放到ptr
                ptr.next = PolyNode(ptr2.coeff, ptr2.power)#將ptr2放到ptr
                ptr2 = ptr2.next
                ptr = ptr.next
            else:
                coef = ptr1.coeff + ptr2.coeff #否則相加
                if coef:
                    ptr.next = PolyNode(coef, ptr1.power)
                    ptr = ptr.next
                ptr1 = ptr1.next #下一筆
                ptr2 = ptr2.next #下一筆
        result.head = result.head.next#最後將算好的結果 第一筆資料放到開頭
        #因為一開始放的是PolyNode 不是真實結果
        return result
                    
poly1 = PolyLL([[2,100], [-3,50], [1,0]])
poly2 = PolyLL([[2,50], [-5,1]])
poly3 = poly1.add(poly2)
poly3.show_poly()

