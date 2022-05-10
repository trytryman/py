a={'key1':1,'key2':3,'key3':2}
b={'key1':1,'key2':4}
for i in a.keys():
   if(a[i]==b.get(i)):
       if i in b.keys():
           print(i,':',a[i])
        

                
    

