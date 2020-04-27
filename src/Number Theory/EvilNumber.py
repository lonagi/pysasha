#Find Evil Numbers

def EvilNumber(num):
    return sum(map(lambda x:1 if '1' in x else 0, str(bin(num))[2:]))%2==0
    
def doTest(toPrint=False,toProgress=False,start=0,toEnd=1000):
    s=set()
    KK=10000
    from IPython.display import clear_output
    for i in range(start,toEnd+1):
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            clear_output(wait=True)
            print(i,end="\t")
        evil=EvilNumber(i)
        if(evil):
            s.add(i)
            if(toPrint and not toProgress):
                print(evil,end=", ")
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            print(s)
    if(not toPrint):
        return s
    
#EvilNumber(3)
#doTest()