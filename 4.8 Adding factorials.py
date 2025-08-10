a = int(input())
s=0
fact=1
for i in range(1,a+1):
    fact*=i
    s+=fact
print(s)