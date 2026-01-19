a=input()
b=a.find('h')
c=a.rfind('h')
first=a[0:b+1]
last=a[c:]
reverse=a[c-1:b:-1]

final=first+reverse+last
print(final)
