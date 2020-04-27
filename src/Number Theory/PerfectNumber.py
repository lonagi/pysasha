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
    s = set()
    KK = 10000
    for i in range(start,toEnd):
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            try:
                from IPython.display import clear_output
            except:
                pass
            clear_output(wait=True)
            print(i,end="\t")
        if((PerfectNumber(i) and isPerfect) or (not PerfectNumber(i) and not isPerfect) ):
            s.add(i)
            if(toPrint and not toProgress):
                print(i,end=", ")
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            print(s)
    if(not toPrint):
        return s
            
doTest(True,True,True,2,20000) #All perfect numbers
print("")
doTest(True,False,False,2,10000) #All non perfect numbers