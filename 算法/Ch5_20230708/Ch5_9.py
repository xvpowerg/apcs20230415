def fibonacci_recrsive(n):
    if n<=0:
       return 0
    elif n== 1 or n==2:
        return 1
    return fibonacci_recrsive(n-1) + fibonacci_recrsive(n-2)
print(f"遞迴:fib({fibonacci_recrsive(20)})")
