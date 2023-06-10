p = [[''] * 5  for i in range(10)]

for i in range(10):
    for j in range(5):
        p[i][j] = f"({i},{j})"

for i in range(10):
    for j in range(5):
        print(p[i][j],end=" ")
    print()    
