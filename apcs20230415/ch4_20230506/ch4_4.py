def weighted_sum(c,e=80,m=60):
    return (c+e*2+m*3)
# 參數過多
#x = weighted_sum(70,80,90,100)
#print(x)
# 參數使用key指定後 後面的參數必須使用key指定
#x = weighted_sum(70,m = 90,80)
#print(x)
# 因為c給過數值了 不能重複給90
#z = weighted_sum(70,80,c=90)
#print(z)
