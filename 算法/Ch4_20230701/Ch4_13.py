count = 0
for i in range(1,7):
    for j in range(1,7):
        if i >= j:
            continue
        for k in range(1,7):
            if j >= k:
                 continue       
            for l in range(1,7):
                if k<l:
                    count+=1
                    print(f"{count:2d} [{i},{j},{k},{l}]")
