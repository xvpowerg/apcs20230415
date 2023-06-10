sum1 = 0

for i in range(1,6):
    sum1 += 2 *i * (3*i+1)
print(sum1)

def sum2(n):
    if n == 1:
        return 8 ##2 *1 * (3*1+1)
    else:
        return sum2(n - 1) + 2 * n *(3 *n +1)
    
print(sum2(5))
