num1 = 10
num2 = 0
nums = [1, 3, 5, 7, 9]
try:
    print(num1 * num3)
    #print(num1 / num2)
    #print(nums[100])
except ZeroDivisionError:
     print("產生例外:ZeroDivisionError")
except NameError:
    print("產生例外:NameError")
except:
    print("Otehr!")
print("程式完成")
