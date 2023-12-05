a=[3,45,7,100]
a.sort()
print(a)
h=len(a)/2
print(h)
if len(a)%2==1:
    h=h-0.5
    h=int(h)
    print(a[h])
else:
    f=h-1
    f=int(f)
    h=int(h)
    print(a[f], a[h])