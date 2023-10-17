a=[]
s='pfdcmhcmdhpfd'
n='pfd'
def first_last(a,s,n):
    if s.find(n)!=-1:
        p=s.find(n)
        l=s.rfind(n)
        a.append(p)
        a.append(l)
        print(a)
        print(len(s))
        
        
first_last(a, s, n)
        
