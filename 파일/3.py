import random
i, k, = 0, 0
a=0
b=0
aStr,bStr = "",""
for i in range(1,21,1):
    k=random.randint(0,1)
    if(k==1):
        aStr+="\u2665"
    else :
        bStr+="\u2665"
print("A=",aStr)
print("B=",bStr)

