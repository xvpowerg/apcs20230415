def gcd_recursive(m, n):
    print('gcd(%d,%d)='%(m,n), end='')
    if n==0:
        return m
    else:
        return gcd_recursive(n, m%n)
n1 = int(input('num1='))
n2 = int(input('num2='))
if(n1<n2):
    n1,n2 = n2,n1
gcd = gcd_recursive(n1, n2)
print(gcd)
