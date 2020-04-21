#Find Keith Number

def KeithNumber(num):
    s=[int(d) for d in str(num)]
    i=0
    l=len(s)
    while s[-1]<num:
        i+=1
        a=0
        for i in range(1,l+1):
            a+=(s[-i])
        s.append(a)
    return s[-1]==num
    
def doTest(toPrint=False,toProgress=False,start=1,toEnd=1000):
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
        if(KeithNumber(i)):
            s.add(i)
            if(toPrint and not toProgress):
                print(i,end=", ")
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            print(s)
    if(not toPrint):
        return s

#KeithNumber(197)
#doTest(True,False,1,10000)
#doTest(True,False,1,100000)