a=22
b=45
def mul_to_int(a,b):
    s=a*b
    if isinstance(s,int):
        print(s,int)
    else:
        print(s,float)
mul_to_int(a,b)