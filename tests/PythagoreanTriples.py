#Pythagorean triples

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

def CompanionPellNumber(index,roundi=True):
    try:
        from sympy import Pow as mmmpow
    except:
        pass
    q = 2**(1/2)
    if(roundi):
        return round(( mmmpow(1+q ,index) - mmmpow(1-q,index) )/2)
    else:
        return ( mmmpow(1+q ,index) - mmmpow(1-q,index) )/2
############################################
    
#Brut Force for all numbers
def _bf(toEnd=30000):
    for a in range(1,toEnd):
        c = ((a**2 + (a+1)**2)**(1/2))
        if(c%1==0):
            print( (a,a+1,int(c)) )

#Brut Force for Even Pell Nums            
def _bfsqr(p = [Binetformula(i,False) for i in range(30) if(i%2!=0 and i!=1)]):
    for y in p:
        y**=2
        d=4-4*2*(1-y)
        x1 = (-2+d**(1/2))//4
        x2 = -((-2-d**(1/2))//4)
        print(x1,x2,y)

#Pythagorean triples from Square triangular numbers with P
def _tfsqtn(toEnd=30):
    for i in range(1,toEnd):
        y = Binetformula(i*2 + 1,False)
        c = y**2
        d=4-4*2*(1-c)
        x1 = (-2+d**(1/2))//4
        x2 = -((-2-d**(1/2))//4)
        print(x1,x2,y)
        
#Pythagorean triples from Square triangular numbers with H
def _tfsqtn2(toEnd=30):
    for n in range(1,toEnd):
        a1 = (CompanionPellNumber(2*n+1,False)-1)//2
        a2 = a1+1
        c = int((a1**2 + a2**2)**(1/2))
        print(a1,a2,c)
        
#Triangular numbers
def _trnums(toEnd=30):
    for n in range(1,toEnd):
        if(n%2==0):
            t = 2 * Binetformula(n)**2
        else:
            t = CompanionPellNumber(n)**2
        s = ((t*(t+1))/2)**(1/2)
        print(int(t),int(t)+1,int(s))
        
#_bf(5000000)

#_tfsqrn(1000) #5.06s
#_bfsqr([Binetformula(i) for i in range(1000) if(i%2!=0 and i!=1)]) #2.42s
#_tfsqtn2(1000) #111ms

#_trnums(10)