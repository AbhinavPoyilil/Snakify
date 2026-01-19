a=input()
first=a[:a.find('h')+1]
mid=a[a.find('h')+1 : a.rfind('h')]
last=a[a.rfind('h'):]
mid=mid.replace('h','H')
print(first+mid+last)
