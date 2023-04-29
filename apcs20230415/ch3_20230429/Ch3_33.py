def c2f(c):    
    return 9 / 5 * c + 32    

while(True):
    inStr = input("輸入攝氏溫度(q離開):")
    if inStr == 'q':
        print("離開")        
        break

    tc = float(inStr)
    
    print(f"華氏溫度:{c2f(tc):.2f}")
