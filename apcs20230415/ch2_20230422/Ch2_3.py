height = float( input("輸入身高 單位公分:"))
weight = int(input("請輸入體重 單位公斤:"))
bmi = weight /  (height/100) ** 2
print("bmi為:",bmi)

print("bmi為:%.2f"%(bmi))
print(f"bmi為:{bmi:.2f}")
rBmi = round(bmi, 2)
print(f"bmi為:{rBmi}")
