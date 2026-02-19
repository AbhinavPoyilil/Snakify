a=int(input())
b=1
ma=0
mb=0
while a!=0:
    if a>ma:
        ma=a
        mb=b
    b=b+1
    a=int(input())
print(mb)    
