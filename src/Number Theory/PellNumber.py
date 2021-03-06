#Pell number   
import numpy as np
def __pow(x, n, I):
    if n==0:
        return I
    elif n == 1:
        return x
    else:
        y = __pow(x,n//2,I)
        y = y.dot(y)
        if n % 2:
            y = x.dot(y)
        return y
    
def PellNumber(index):
    F = __pow(np.array(((2,1),(1,0)),dtype=object),index,np.eye(2))
    return F[0][1]

def Binetformula(index=1,roundi=True):
    from sympy import Pow as mmmpow
    from sympy import Integer as mmmint
    from sympy import N as mmmn
    q = 2**(1/2)
    r = (mmmpow(1+q,index)-mmmpow(1-q,index))/(2*q)
    if(roundi):
        return mmmint(r)
    else:
        return mmmn(r)

#Pell–Lucas
def CompanionPellLucasNumber(Pell,roundi=True):
    from sympy import Integer as mmmint
    from sympy import N as mmmn
    r = Pell*(2**(1/2))
    if(roundi):
        return mmmint(r)
    else:
        return mmmn(r)

def CompanionPellNumber(index=1,roundi=True):
    from sympy import Pow as mmmpow
    from sympy import Integer as mmmint
    from sympy import N as mmmn
    q = 2**(1/2)
    r = (mmmpow(1+q,index)-mmmpow(1-q,index))/(2)
    if(roundi):
        return mmmint(r)
    else:
        return mmmn(r)

def PellNumbers(toEnd):
    Pells=[1,2,5]
    i=3
    while i<toEnd:
        num=Pells[i-1]*2+Pells[i-2]
        Pells.append(num)
        i+=1
    return Pells
    
def doTest(toPrint=False,toProgress=False,start=0,toEnd=1000,algo="s"):
    s = set()
    KK = 10000
    from IPython.display import clear_output
    for i in range(start,toEnd+1):
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            clear_output(wait=True)
            print(i,end="\t")
        if(algo=="s"):
            pell = PellNumber(i)
        elif(algo=="binet"):
            pell = Binetformula(i)
        elif(algo=="companion"):
            pell = CompanionPellNumber(i)
        elif(algo=="pelllucas"):
            pell = CompanionPellLucasNumber(i)
        if(pell):
            s.add(pell)
            if(toPrint and not toProgress):
                print(pell,end=", ")
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            print(s)
    if(not toPrint):
        return s

#print(Binetformula(6))
#print(PellNumber(6))
#doTest(True,False,0,10000)