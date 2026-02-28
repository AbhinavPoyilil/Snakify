a=-1
max=0
count=0
while a!=0:
    a=int(input())
    if a>max:
        max=a
        count=1
    elif a==max:
        count+=1
print(count)        
