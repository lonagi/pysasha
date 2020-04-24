#Lucas number

def LucasNumber(index,roundi=True):
    from sympy import Pow as mmmpow
    b = (mmmpow(((1+5**(1/2))/2),index))+(mmmpow(((1-5**(1/2))/2),index))
    if(roundi):
        return round(b)
    else:
        return b

def LucasSequence(index,returni=False):
    from sympy import Pow as mmmpow
    b = (mmmpow(((1+5**(1/2))/2),index))+(mmmpow(((1-5**(1/2))/2),index))
    if(roundi):
        return round(b)
    else:
        return b
    
def isLucas(num):
    try:
        if("math" not in sys.modules):
            try:
                from math import log as mlog
            except:
                pass
    except:
        import sys
        from math import log as mlog
    a = 2.07684408521711*mlog(2.237*num)
    return (a % 1 * 100 > 90) or (a % 1 * 100 < 5)

def isPrime_Lucas(num):
    pass

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
            lucas = LucasNumber(i)
        if(lucas):
            s.add(lucas)
            if(toPrint and not toProgress):
                print(lucas,end=", ")
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            print(s)
    if(not toPrint):
        return s
                
#LucasNumber(0)
#doTest(True,False,0,200)