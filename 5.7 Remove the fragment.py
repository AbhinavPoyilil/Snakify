a=input()
b=a.find('h')
c=a.rfind('h')
print(a[0:b]+a[c+1::])