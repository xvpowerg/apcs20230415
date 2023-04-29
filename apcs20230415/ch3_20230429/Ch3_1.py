carList = ['Audi', 'Toyota', 'Benz', 'BMW', 'Mazda', 'Ford', 'BMW', 'Benz', 'BMW', 'Mazda']
carSet  = {'Audi', 'Toyota', 'Benz', 'BMW', 'Mazda', 'Ford', 'BMW', 'Benz', 'BMW', 'Mazda'}

# 輸入一個整數取得汽車品牌
indx = int(input("請輸入第幾筆車:"))
print(carList[indx - 1])
# 輸出所有汽車品牌
for car in carSet:
    print(car)
# Audi / Benz / BMW 出現在carList次數
LuxuryCar  = ("Audi", "Benz", "BMW")
LuxuryCarDict = {"Audi":0,"Benz":0,"BMW":0}
for car in carList:
    if car in LuxuryCar:
        LuxuryCarDict[car] += 1
print(LuxuryCarDict)
