sum1 = 0
for i in range(1,101):
    sum1 += i
print(sum1)    

def incrementSum(n):
    
    if n == 1:
        return 1
    else:
        return incrementSum(n - 1) + n
print(incrementSum(100))    


sum2 = 0
for j in range(1,11):
    sum2 += j * j
print("1~10平方和:")
print(sum2)

def squareSum(n):
    if n == 1:
        return 1
    else:
        return squareSum(n - 1) + n * n
print("=",squareSum(10))
