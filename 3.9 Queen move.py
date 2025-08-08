x = int(input())
y = int(input())
xn = int(input())
yn = int(input())

if yn==y or xn==x or (abs(xn-x)==abs(yn-y)):
    print('YES')
else:
    print("NO")