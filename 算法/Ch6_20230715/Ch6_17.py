treasures = [50,160,20,100,20,60,90,120,150,30]
treasures.sort()
print(treasures)
shipLoad = []
total = 0
capcity = 500
for treasure in treasures:
    if treasure + total < capcity:
        shipLoad.append(treasure)
        total += treasure
        
print(f"總重量{total}公斤")
print(f"船上共{len(shipLoad)}個寶物")
