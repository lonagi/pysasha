#Find Silver Ratio

import sympy as sp

def Binetformula(index,roundi=True):
    try:
        from sympy import Pow as mmmpow
    except:
        pass
    q = 2**(1/2)
    if(roundi):
        return round(( mmmpow(1+q ,index) - mmmpow(1-q,index) )/(2*q))
    else:
        return ( mmmpow(1+q ,index) - mmmpow(1-q,index) )/(2*q)

def CompanionPellNumber(Pell,roundi=True):
    if(roundi):
        return round(Pell * (2**(1/2)))
    else:
        return round(Pell * (2**(1/2)))
    
s = set()
for i in range(100):
    a = sp.Float(Binetformula(i,False))
    b = sp.Float(CompanionPellNumber(a))
    c = b+a*(2**(1/2))
    print(c, end=", ")
    s.add(c)
#s