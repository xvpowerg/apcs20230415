def testAsc(arr):
    for i in range(len(arr) - 1):
        if arr[i] >=arr[i+1]:
           print("不是遞增!")
           break
    else:
        print("遞增陣列")

def test2(arr):
    for i in range(len(arr) - 1):
        if arr[i] * arr[i + 1] >= 0 :
            print("不是正負交錯")
            break
    else:
            print("是正負交錯")
num = int(input("輸入陣列個數:"))

arr = []
for i in range(num):
    v = int(input(f"輸入第{i+1}數值:"))
    arr.append(v)
#testAsc(arr)
test2(arr)
