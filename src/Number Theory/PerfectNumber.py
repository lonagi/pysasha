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
#findSuperPerfectNumbers()
#findAllSuperPerfectNumbers()


#PerfectNumber(28)
#AbundantNumber(18)
#DeficientNumber(23)
#Quasiperfect(20)
#AlmostPerfectNumber(32)
#SemiPerfectNumber(12)
#SuperPerfect(64)