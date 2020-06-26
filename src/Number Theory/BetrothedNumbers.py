#Betrothed Numbers

#TOOLS
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
#############################

##Brute force Method
def BetrothedNumber(k,ratio=5.5,ratio2=5.5,order=1,returni=False):  
    ##All divisors for all numbers
    allDels=dict()
    
    ###Second number is greater than first number
    from itertools import chain
    concatenated = chain( range(k, int(k*ratio)+1 ),range(k, int(k/ratio2)+1 ,-1) )
    for i in concatenated:

        ###We don't want repeat operations
        ###Therefore search and save all divisors
        if(str(i) not in allDels):
            allDels[str(i)] = Divisors(i)

        ###Sum1+order_num = 2nd Num and Sum2+order_num = 1st Nub
        if(i != k and sum(allDels[str(i)]) == k+order and sum(allDels[str(k)]) == i+order):
            if(returni):
                return (k,i)
            else:
                print(k,"->",i)

def BetrothedNumbers(m,n,order=1):
    if(m!=n):
        s1=set([1])
        for i in range(int(m/2+1),1,-1):
            if(m%i==0):
                s1.add(i)
        s2=set([1])
        for i in range(int(n/2+1),1,-1):
            if(n%i==0):
                s2.add(i)
        return sum(s1)==n+1 and sum(s2)+n==sum(s1)+m
    else:
        return False
        
def doTest(toPrint=False,toProgress=False,start=1,toEnd=1000,algo="bf"):
    s=set()
    KK=10000
    from IPython.display import clear_output
    for i in range(start,toEnd+1):
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            clear_output(wait=True)
            print(i,end="\t")
        if(algo=="bf"):
            bet=BetrothedNumber(i)
        if(bet):
            s.add(bet)
            if(toPrint and not toProgress):
                print(bet,end=", ")
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            print(s)
    if(not toPrint):
        return s
                
#BetrothedNumber(48)
#BetrothedNumbers(140,195)
#doTest()