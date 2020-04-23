#Find Bell Numbers

def BellNumber(index): 
    bell = [[0 for i in range(index+1)] for j in range(index+1)] 
    bell[0][0] = 1
    for i in range(1, index+1): 
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1] 
    return bell[index][0]

def _BellNumber(index,dps=30):
    try:
        import mpmath
    except:
        pass
    mpmath.mp.dps = dps
    return int(mpmath.bell(index))
    
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
            bell = BellNumber(i)
        elif(algo=="mpmath"):
            bell = _BellNumber(i)
        if(bell):
            s.add(bell)
            if(toPrint and not toProgress):
                print(bell,end=", ")
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            print(s)
    if(not toPrint):
        return s
  
#BellNumber(2000)
#_BellNumber(2000,dps)
#doTest(False,False,1,500) #7.97s
#doTest(False,False,1,500,"mpmath") #1.73s