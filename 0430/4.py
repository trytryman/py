import random
t=[]
m=[]
b=[]
for i in range(0,150,1):
    무게=random.randrange(300,700)
    당도=random.randrange(7,12)
    if(무게>=600):
        if(당도>=10):
            t.append(i)
        elif(10>당도>8):
            m.append(i)
        else:
            b.append(i)
    elif(600>무게>400):
        if(당도>=10):
            m.append(i)
        else:
            b.append(i)
    else:
        b.append(i)
print('상급=',len(t),'개',t)
print('중급=',len(m),'개',m)
print('하급=',len(b),'개',b)
        
        