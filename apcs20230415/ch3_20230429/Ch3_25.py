results = {"David":0,"Amy":0,"Sean":0}
users = ("David","Amy","Sean")

for i in range(5):
    vote = input("投票給:")
    if  vote  not in users:
        print("票無效")
        continue
    results[vote] += 1

print("選舉結果:")
for name in users:    
    print(name,results[name])
