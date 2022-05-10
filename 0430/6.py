x=""
x=input()
y=len(x)
num=0
sm=0
bi=0
ko=0
etc=0
for i in x:
    if(i.isdigit()==True):
        num=num+1
    if(i.islower()==True):
        sm=sm+1
    if(i.isupper()==True):
        bi=bi+1
    if(i.encode().isalpha()==True):
        ko=ko+1
    else:
        etc=etc+1
print('대문자=',bi,'소문자=',sm,'숫자=',num,'한글=',ko,'기타',etc)
print(y)
        
        
        
    