def LucasNumber(index,roundi=True):
    from sympy import Pow as mmmpow
    from sympy import Integer as mmmint
    b = (mmmpow(((1+5**(1/2))/2),index))+(mmmpow(((1-5**(1/2))/2),index))
    if(not roundi):
        return mmmint(b)
    else:
        return b

def isPrime_Lucas(p):
    l = LucasNumber(p,True)
    if((l-1)%p!=0):
        return l

with open("file","r") as f:
    a=f.read()
print(isPrime_Lucas(int(a)))