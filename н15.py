a = ['Петя','Иоган','Филипп']
b = ['Петя','Иоган']
c = ['Петя','Иоган','Филипп']
for i in range(len(a)):
    t = a[i]
    print(t)
    for y in range(len(b)):
        r = b[y]
        if t == r:
            c.pop(i)       
print(c)
            