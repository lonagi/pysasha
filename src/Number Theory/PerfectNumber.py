#Find Perfect Numbers

##TOOLS
def Divisors(num):
    s = set([1])
    for i in range( int(num/2 + 1),1,-1):
        if(num%i==0):
            s.add(i)
    return s

##THE PROGRAM
def PerfectNumber(num):
    d = Divisors(num)
    return sum(d)==num
             
def doTest(toPrint=False,start=2,toEnd=1000):
    s = set()
    for i in range(start,toEnd):
        if(PerfectNumber(i)):
            s.add(i)
            if(toPrint):
                print(i,end=", ")
    return s
            
doTest(True,2,10000)