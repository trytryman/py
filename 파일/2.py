x=0
y=1
z=0
while True:
    x=int(input("성적:"))
    if(100>x>0):
        z=x/y
        print("평균점수",z)
        y=y+1
    else :
        print("최종평균점수",z)
        break
