#Find Perfect Numbers

##TOOLS
def Divisors(num): 
    from math import sqrt as mmsq
    s=set([1])
    i=1
    a=int(mmsq(num)+1)
    while i<=a: 
        if(num//i==num):
            i+=1
            continue
        if (num%i==0): 
            if (num//i!=i): 
                s.add(num//i)
            s.add(i)
        i+=1
    return s
def _makeSett(comb):
    a=comb
    b=set()
    k=0
    for j in range(1,len(a)*2):
        a=comb.copy()
        for i in range(0,len(a)):
            b.add(tuple(a[i::j]))
        for i in range(0,len(a)-1):
            b.add(tuple(a[i::-1*j]))
        for i in range(0,len(a)):
            b.add(tuple(a[i:len(a)-j:j]))
        for i in range(0,len(a)-1):
            b.add(tuple(a[i:len(a)-j:-1*j]))
        try:
            a.pop(j-1)
        except:
            pass
        b.add(tuple(a))
    return b
############################

##THE PROGRAM
def PerfectNumber(num):
    return sum(Divisors(num))==num

def AbundantNumber(num):
    return sum(Divisors(num))>num

def DeficientNumber(num):
    return sum(Divisors(num))<num

def QuasiPerfectNumber(num):
    return sum(Divisors(num))-num==1

def AlmostPerfectNumber(num):
    return sum(Divisors(num))-num==-1

def SemiPerfectNumber(num):
    dv=sorted(Divisors(num))
    for i in _makeSett(dv):
        if(sum(i)==num):
            return True
    return False
    
def SuperPerfect(n,m=2,k=2):
    dv=sum(Divisors(n))+n
    for i in range(m-1):
        dv=sum(Divisors(dv))+dv
    return dv==k*n

def doTest(toPrint=False,toProgress=False,start=0,toEnd=1000,algo="perfect"):
    s=set()
    KK=10000
    from IPython.display import clear_output
    for i in range(start,toEnd+1):
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            clear_output(wait=True)
            print(i,end="\t")
        if(algo=="perfect"):
            pf=PerfectNumber(i)
        elif(algo=="abundant"):
            pf=AbundantNumber(i)
        elif(algo=="deficient"):
            pf=DeficientNumber(i)
        elif(algo=="quasi"):
            pf=Quasiperfect(i)
        elif(algo=="almost"):
            pf=AlmostPerfectNumber(i)
        elif(algo=="semi"):
            pf=SemiPerfectNumber(i)
        elif(algo=="super"):
            pf=SuperPerfect(i)
        if(pf):
            s.add(i)
            if(toPrint and not toProgress):
                print(i,end=", ")
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            print(s)
    if(not toPrint):
        return s

#PerfectNumber(28)
#AbundantNumber(18)
#DeficientNumber(23)
#Quasiperfect(20)
#AlmostPerfectNumber(32)
#SemiPerfectNumber(12)
#SuperPerfect(64)

#doTest(True,False,0,20000) #348 ms
#doTest(True,False,0,20000,"abundant")
#doTest(True,False,0,20000,"deficient")
#doTest(True,False,0,20000,"quasi")
#doTest(True,False,0,20000,"almost")
#doTest(True,False,0,5000,"semi")
#doTest(True,False,0,20000,"super")