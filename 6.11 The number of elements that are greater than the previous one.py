a=int(input()) 

count=0
while a!=0:
    temp=a
    a=int(input())
    if a>temp:
        count+=1
print(count)        
