k = int(input())
for i in range(1,k+1):
    for j in range(1,i+1,--1):
        print(j,sep='',end='')
    print()    
