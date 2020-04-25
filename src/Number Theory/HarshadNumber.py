#Find Harshad Numbers

def getDigits(a):
    s=set()
    while a:
        s.add(a%10)
        a//=10
    return s

def HarshadNumber(num):
    sum=0
    for i in getDigits(num):
        sum+=i
    return num%sum==0

def doTest(toPrint=False,toProgress=False,start=9,toEnd=1000):
    s=set()
    KK=10000
    from IPython.display import clear_output
    for i in range(start,toEnd+1):
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            clear_output(wait=True)
            print(i,end="\t")
        if(HarshadNumber(i)):
            s.add(i)
            if(toPrint and not toProgress):
                print(i,end=", ")
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            print(s)
    if(not toPrint):
        return s

#print(doTest(False,False,10,10000))
#doTest(True,False,10,15000)