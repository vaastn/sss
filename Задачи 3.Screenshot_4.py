a = 'a 32 t 4321 l 35 v'
d=0
a=a.split()
summ = 0
for i in a:
    if i.isdigit():
        summ+=int(i)
print(summ)