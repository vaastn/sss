a=[]
def blin(a):
  n=int(input('Введите число'))
  a.append(n)
  print(a)
def trash(a):
    for i in range (len(a)):   
        if a[i]%3 == 0:
            print(a[i])
while True:
    s=int(input('1 или 2'))
    if s==1:
      blin(a)
    elif s==2:
     trash(a)
    else:
        print('нет такого варианта')