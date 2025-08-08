x = int(input())
y = int(input())
xn = int(input())
yn = int(input())

if (xn-2==x and (yn-1==y or yn+1==y)) or (yn-2==y and (xn-1==x or xn+1==x)) or (xn+2==x and (yn-1==y or yn+1==y)) or (yn+2==y and (xn-1==x or xn+1==x)):
    print('YES')
else:
    print('NO')