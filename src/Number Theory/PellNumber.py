#Pell number   
try:
    import numpy as np
except:
    pass
def pow(x, n, I):
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x,n//2,I)
        y = y.dot(y)
        if n % 2:
            y = x.dot(y)
        return y
    
def PellNumber(index):
    F = pow(np.array(((2,1),(1,0)),dtype=object),index,np.eye(2))
    return F[0][1]

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

#Pell–Lucas
def CompanionPellLucasNumber(Pell,roundi=True):
    r = Pell * (2**(1/2))
    if(roundi):
        return round(r)
    else:
        return r

def CompanionPellNumber(index,roundi=True):
    q = 2**(1/2)
    r = ((1+q)**index + (1-q)**index)/2
    if(roundi):
        return round(r)
    else:
        return r

def PellNumbers(toEnd):
    import time
    Pells = [1,2,5]
    i = 3
    while i < toEnd:
        num = Pells[i-1]*2 + Pells[i-2]
        Pells.append(num)
        i+=1
    return Pells
    
def doTest(toPrint=False,toProgress=False,start=0,toEnd=1000,algo="s"):
    s = set()
    KK = 10000
    for i in range(start,toEnd+1):
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            try:
                from IPython.display import clear_output
            except:
                pass
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
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            print(s)
    if(not toPrint):
        return s

#print(Binetformula(6))
#print(PellNumber(6))
#doTest(True,False,0,10000)