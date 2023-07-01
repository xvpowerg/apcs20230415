'''
質因數分解
引用埃拉斯托特尼篩法，檢查範圍改為2到√ x 
'''
from math import sqrt
while True:
    n= int(input("輸入一個整數:"))
    if n== -1:
        break
    print(f"{n}=",end='')
    while True:
        for i in range(2,int(sqrt(n)) + 1):
            if n %i == 0:
                n = int(n /i)
                print(f"{i}*",end='')    
                break
        else:
            print(n)
            break    
