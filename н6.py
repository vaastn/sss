n=1
a="14, 2, 10"
a="14, 2, 10".split(', ')
a=map(int,a)
a=list(a)
for i in a:
    n=n*i
print(n)