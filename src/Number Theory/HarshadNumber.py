def HarshadNumber(num):
    sum=0
    for i in list(str(num)):
        sum+=int(i)
    return num % sum==0

def doTest(toPrint=False,toProgress=False,start=2,toEnd=1000):
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
        if(HarshadNumber(i) ):
            s.add(i)
            if(toPrint and not toProgress):
                print(i,end=", ")
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            print(s)
    if(not toPrint):
        return s

#print(doTest(False,False,10,10000))
#doTest(True,True,10,1500)