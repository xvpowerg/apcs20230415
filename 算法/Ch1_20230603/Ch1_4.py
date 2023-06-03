def dec_to_bin(num):
    l = []
    while True:
       num,mod = divmod(num,2)
       l.append(str(mod))
       if  num == 0:
           return "".join(l[::-1])

def def_to_oct(num):
    l = []
    if  num < 0: return "-"+dec_to_bin(abs(num))
    while True:
        num,mod = divmod(num,8)
        l.append(str(mod))
        if num == 0:
            return "".join(l[::-1])
def def_to_hex(num):
    l = []
    base = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    while True:
       num,mod = divmod(num,16)
       l.append(base[mod])
       if num == 0:
           return "".join(l[::-1])

print(dec_to_bin(19))
print(def_to_oct(19))
print(def_to_hex(31))
