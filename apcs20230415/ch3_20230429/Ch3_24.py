count = 1
answer = 5
guess = int(input("猜一個數字"))

while count < 5:
    if guess == answer:
        print("猜對了")
        break        
    count += 1
    guess = int(input("再猜一次"))
print("遊戲結束")    
