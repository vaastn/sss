a = '12, 13, 43, 24, 65'
a = '12, 13, 43, 24, 65'.split(", ")
a=map(int,a)
a=list(a)
g=0
for i in range(len(a)):
    print(a)
    n=a[i]
    g+=n
print(g)
    