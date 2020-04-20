#Almost perfect numbers

def isAlmostPerfectNumber(n):
    s = set([1])
    for j in range(int(n/2+1),1,-1):
        if(n % j==0):
            s.add(j)
    return sum(s)+1==n

def doTest(toPrint=False,start=2,toEnd=1000):
    s = set()
    for i in range(start,toEnd):
        if(isAlmostPerfectNumber(i)):
            s.add(i)
    if(toPrint):
        print(s)
    else:
        return s

#isAlmostPerfectNumber(i)
doTest(True,2,100000)