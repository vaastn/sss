a=[0,1,2,3,4]
b=a[0]
a[0]=a[len(a)-1]
a[len(a)-1]=b
print(a)