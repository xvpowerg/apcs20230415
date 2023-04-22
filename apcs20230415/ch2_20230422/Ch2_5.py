ch = int(input("國文成績:"))
ma = int(input("數學成績:"))
en = int(input("英文成績:"))

total = ch + ma + en
print("總成績:",total)
print('平均分數:%.2f'%(total/3))
print(f'平均分數:{total/3:.2f}')
