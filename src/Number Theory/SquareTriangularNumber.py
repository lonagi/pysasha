#Find Square triangular numbers

def SquareTriangularNumber(k,roundi=True):
    r = ((((3 + 2 * (2)**(1/2))**(k))-((3 - 2 * (2)**(1/2))**(k)))/(4 * (2)**(1/2)))**2
    if(roundi):
        return round(r)
    else:
        return r

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
            sqrnn = SquareTriangularNumber(i)
        if(sqrnn):
            s.add(sqrnn)
            if(toPrint and not toProgress):
                print(sqrnn,end=", ")
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            print(s)
    if(not toPrint):
        return s    
    
#SquareTriangularNumber(2)
#doTest(True,True,0,100)