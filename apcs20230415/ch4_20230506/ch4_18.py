h = float(input('請輸入身高，單位為公分: '))
w = int(input('請輸入體重，單位為公斤: '))
def calcBmi(h,w):
    bmi = w/((h/100)**2)
    return bmi

def statusMsg(bmi):
    result = '數值錯誤'
    if(bmi>30):
     result = '肥胖'
    elif(bmi>25):
     result = '過重'
    elif(bmi>18.5):
     result = '正常'
    elif(bmi>0):
     result = '過輕'
    return result
bmi = calcBmi(h,w)
result = statusMsg(bmi)
print(result) 
    
