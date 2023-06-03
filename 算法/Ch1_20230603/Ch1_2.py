"""
print(chr(65))
print(chr(65+1))
print(chr(65+2))
print(chr(65+3))
print(chr(65+4))
"""

for i in range(5):    
    print(" " * (4-i),chr(65 + i)*(2*i+1),sep="")
