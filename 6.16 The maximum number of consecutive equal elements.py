a=-1
count=0
ncount=0
temp=-1
while a!=0:
    a=int(input())
    
    if a==temp:
        count+=1
        if count>ncount:
            ncount=count
    else:
        count=0
    temp=a    
print(ncount+1)        
