coinType = (50,10,5,1)
def exchange(amt):
    global count
    result = {}
    for coin in coinType:
        num = amt // coin
        result[coin] = num
        count += num
        amt %= coin
    return result

count = 0
amount = int(input("輸入兌換金額"))
answer = exchange(amount)
for coin in coinType:    
    print(f"{coin}元硬幣:{answer[coin]}")

print(f"共換成{count}枚硬幣")
