#Lucas number

def LucasNumber(index,roundi=True):
    from sympy import Pow as mmmpow
    from sympy import Integer as mmmint
    b = (mmmpow(((1+5**(1/2))/2),index))+(mmmpow(((1-5**(1/2))/2),index))
    if(not roundi):
        return mmmint(b)
    else:
        return b

def LucasSequence(countt,returni=True):
    s = [2,1]
    for n in range(2,countt):
        s.append(s[n-1]+s[n-2])
    if(returni):
        return s
    else:
        print(s)

def isPrime_Lucas(p,roundi=True):
    l = LucasNumber(p,roundi)
    if((l-1)%p!=0):
        return l

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
        elif(algo=="prime"):
            lucas = isPrime_Lucas(i)
        if(lucas):
            s.add(lucas)
            if(toPrint and not toProgress):
                print(lucas,end=", ")
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            print(s)
    if(not toPrint):
        return s
                
#LucasNumber(0)
#doTest(True,False,0,800) #1.69 s
#LucasSequence(800) #30 ms
#isPrime_Lucas(10)
#doTest(False,False,1,10000,"prime")