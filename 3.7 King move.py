x= int(input())
y= int(input())
x1= int(input())
y1= int(input())
if (x1==x+1 or x1==x-1) and (y1==y+1 or y1==y-1):
    print('YES')
elif (x1==x and (y1==y+1 or y1==y-1)) or (y1==y and (x1==x-1 or x1==x+1)):
    print('YES')
else:
    print('NO')