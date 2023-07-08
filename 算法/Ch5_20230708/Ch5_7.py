def factorial_recursive(n):
    #print_process(N, n)
    if n==1:        
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(4))
