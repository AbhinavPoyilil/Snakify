a=int(input())
f2=0
f1=1
count=0

while f2<a:
    f2,f1=f1,f1+f2
    count+=1

if f2>a:
    print(-1)
else:
    print(count)
