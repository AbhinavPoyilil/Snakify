a=int(input())
if a==0:
    print(0)
else:
    n2,n1=0,1
    for i in range(2,a+1):
        n2,n1=n1,n1+n2
    print(n1)    
