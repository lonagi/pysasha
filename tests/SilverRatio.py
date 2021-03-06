#Find Silver Ratio

import sympy as sp

def Binetformula(index,roundi=True):
    try:
        from sympy import Pow as mmmpow
    except:
        pass
    q = 2**(1/2)
    r = ( mmmpow(1+q ,index) - mmmpow(1-q,index) )/(2*q)
    if(roundi):
        return round(r)
    else:
        return r
    
s = set()
q = 2**(1/2)
for i in range(100):
    a = sp.Float(Binetformula(i,False))
    b = sp.Float(Binetformula(i)*q)
    c = b+a*(2**(1/2))
    print(c, end=", ")
    s.add(c)
#s