#Find Catalan Numbers

def CatalanNumber(index):
    try:
        from math import factorial as f
    except:
        pass
    return f(2*index) // ( f(index) * f(index+1)  )

def doTest(toPrint=False,toProgress=False,start=0,toEnd=1000):
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
        ct = CatalanNumber(i)
        if(ct ):
            s.add(ct)
            if(toPrint and not toProgress):
                print(ct,end=", ")
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            print(s)
    if(not toPrint):
        return s

#CatalanNumber(3)
#doTest(True) #222 ms

### SYMPY func!!!!! 4.01 s
#import sympy as sp
#for i in range(0,1001):
#    sp.catalan(i)