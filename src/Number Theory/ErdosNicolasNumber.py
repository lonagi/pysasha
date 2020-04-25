########## Erdős–Nicolas number

#TOOLs
def Divisors(num): 
    s=set()
    i=1
    a=num**(1/2)
    while i<=a: 
        if (num%i==0): 
            if (num/i==i): 
                s.add(i)
            else: 
                s.add(i)
        i+=1
    return s
def PerfectNumber(num):
    return sum(Divisors(num))==num

#
##THE PROGRAM
def ErdosNicolas_Number(num):
    if(not PerfectNumber(num)):
        s = list(Divisors(num))
        s.sort()
        for i in s:
            if(sum(s) < num):
                break
            elif(sum(s)==num):
                return True
            s.pop()
        return False
    else:
        return False
    
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
        if(ErdosNicolas_Number(i) ):
            s.add(i)
            if(toPrint and not toProgress):
                print(i,end=", ")
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            print(s)
    if(not toPrint):
        return s
    
#print(ErdosNicolas_Number(24))
doTest(True,False,2,43000)