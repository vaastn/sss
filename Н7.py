a=[[12,23,13],[12,34,22],[23,12,33]]
d=0
for i in range(len(a)):
    s=1
    h=a[i]
    for k in range(len(h)):
        s=s*h[k]
        print(s)
    d+=s
print(d)    