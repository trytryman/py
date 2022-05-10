import random
y=0
x=[y]
d={}
z=0
for y in range(1,10,1):
    y=random.randrange(1,100)
    x.append(y)
    if(y>70):
        z=x.index(y)
        d[z]=y
print(x)
x.sort()
print("최대값=",x[-1],"최소값=",x[0])    
print(d)
