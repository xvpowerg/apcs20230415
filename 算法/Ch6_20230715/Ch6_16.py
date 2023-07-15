bottleType = (30,18,5,1)
def exchange(amt):
    global count
    result = {}
    for botle in bottleType:
        num = amt // botle
        result[botle] = num
        count += num
        amt %= botle    
    return result

count = 0
amount = int(input("輸入水量"))
ans = exchange(amount)
for bottle in bottleType:
    print(f"{bottle}公升容量{ans[bottle]}個")
    
print(f"共使用{count}個容器")
