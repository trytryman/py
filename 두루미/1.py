x=0
y=0
z=0
x=int(input("숫자"))
for x in range(1,x+1,1):
    y=x+y
print("합계:",y)
while True:
    x=x-1
    if(x%2==0):
        y=y-x
    if(x==0):
        break
print("홀수의 합계:",y)

    