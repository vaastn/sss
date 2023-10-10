a="ассоциативность"
b="дистрибутивность"
c="коммутативность"
d="правило де Моргана"
n=input("введите значение")
def help_bool(a,b,c,d,n):
    if n=='a':
        print(a)
    elif n=='b':
        print(b)
    elif n=='c':
        print(c)
    elif n=='d':
        print(d)
    else:
        print("мимо")
help_bool(a,b,c,d,n)