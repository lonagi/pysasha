def getGoldenRatio():
    return((5**(1/2)) + 1)/2

def GoldenNumber(index=1,Pair=False,roundi=True):
    try:
        from sympy import Pow as mmmpow
    except:
        pass
    q = 5**(1/2)
    pp = getGoldenRatio()
    r = ((mmmpow(pp,index) - mmmpow(-pp,-index))/q)
    if(roundi):
        if(Pair):
            return (NextGoldenNumber(round(r)),round(r))
        else:
            return round(r)
    else:
        if(Pair):
            return (NextGoldenNumber(r,False,False),r)
        else:
            return r
    
#Companion Golden Number
def NextGoldenNumber(Golden,Pair=False,roundi=True):
    r=Golden*getGoldenRatio()
    if(roundi):
        if(Pair):
            return (Golden,round(r))
        else:
            return round(r)
    else:
        if(Pair):
            return (Golden,r)
        else:
            return r

def GoldenFractions(toEnd=100):
    pp = getGoldenRatio()
    for i in range(1,toEnd):
        a = i*pp
        if(a%1 *100 <10):
            print((int(a),i),end=', ')
            
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
            gold = GoldenNumber(i)
        elif(algo=="pairs"):
            gold = GoldenNumber(i,True)
        if(gold):
            s.add(gold)
            if(toPrint and not toProgress):
                print(gold,end=", ")
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            print(s)
    if(not toPrint):
        return s

#GoldenNumber(8)
#NextGoldenNumber(34)
#GoldenRatio(100)
#doTest(False,False,1,100,"pairs")
#doTest(False,False,1,100)