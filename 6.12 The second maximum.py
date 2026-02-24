a=-1
maxi=0
prevmax=0

while a!=0:
    a=int(input())
    if a>maxi:
        prevmax=maxi
        maxi=a
    elif a>prevmax:
        prevmax=a
print(prevmax)        
    
