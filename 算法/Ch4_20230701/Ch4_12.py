c = 65
for i in range (0,5):
    for j in range(0,5):
        if i == j:
            continue
        for k in range(0,5):
            if i == k or j == k:
                continue
            for l in range(0,5):
              if l == k or l == j or l == i:
                 continue
              for m in range(0,5):
                   if m == k or m == j or m == i or m == l:
                         continue
                   print(f"[{chr(c+i)},{chr(c+j)},{chr(c+k)},{chr(c+l)},{chr(c+m)}]")
