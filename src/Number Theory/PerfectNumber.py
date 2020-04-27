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

def SemiPerfectNumber(n):
    factors = Divisors(n)
    if(sum(factors)==n):
        return True
    factors = list(factors)[:-1]
    num_factors = len(factors)
    subset = [[0 for i in range(n + 1)]for j in range(num_factors + 1)]
    for i in range(num_factors + 1):
        subset[i][0]= True
    for i in range(1, n + 1):
        subset[0][i] = False
    for i in range(1, num_factors + 1):
        for j in range(1, n + 1):
            if j < factors[i - 1]:
                subset[i][j] = subset[i - 1][j]
            else:
                subset[i][j] = subset[i - 1][j] or subset[i - 1][j - factors[i - 1]]
    if subset[num_factors][n] == 0:
        return False
    return True

def HemiPerfectNumber(num):
    dv=sum(Divisors(num))+num
    return (dv*2/num) % 1 * 100==0 and (dv*2/num)%2!=-0
    
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
        elif(algo=="hemi"):
            pf=HemiPerfectNumber(i)
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
#HemiPerfectNumber(24)
#SuperPerfect(64)

#doTest(True,False,0,20000) #348 ms
#doTest(True,False,0,20000,"abundant")
#doTest(True,False,0,20000,"deficient")
#doTest(True,False,0,20000,"quasi")
#doTest(True,False,0,20000,"almost")
#doTest(True,False,0,5000,"semi")
#doTest(True,False,1,5000,"hemi")
#doTest(True,False,0,20000,"super")