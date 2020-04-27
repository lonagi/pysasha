#Amicable numbers

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

def _isPrime(n):
    if n%2==0:
        return n==2
    d=3
    while d*d<=n and n%d!=0:
        d+=2
    return d*d>n   

####################################

##Brute force Method
def AmicableNumber(k,returni=False):  
    ##All divisors for all numbers
    allDels = dict()
    
    ###Second number is greater than first number
    from itertools import chain
    concatenated = chain( range(k, int(k*2.5)+1 ),range(k, int(k/3)+1 ,-1) )
    for i in concatenated:

        ###We don't want repeat operations
        ###Therefore search and save all divisors
        if(str(i) not in allDels):
            allDels[str(i)] = Divisors(i)
                    
        ##Sum1 = 1st_num and Sum2 = 2nd_num
        if(i != k and sum(allDels[str(i)]) == k and sum(allDels[str(k)]) == i):
            if(returni):
                return (k,i)
            else:
                print(k,"->",i)             
                
def Formula_Sabita_ibn_Kurra(n):    
    p = (3 * 2**(n-1)) - 1
    q = (3 * 2**n) - 1
    r = (9 * 2**(2*n-1))-1
    
    if(_isPrime(p) and _isPrime(q) and _isPrime(r)):
        return ( 2**n * p * q, 2**n * r )
    
def Walter_Borough(n,A=220,a=4,u=55,s=71):
    p = s+u+1
    q1 = (u+1)*p**n - 1
    if(_isPrime(q1)):
        q2 = (u+1)*(s+1)*p**n - 1
        if(_isPrime(q2)):   
            return ( A*p**n *q1, a*p**n *q2 )

def doTest(toPrint=False,start=2,toEnd=1000,algo="bf"):
    allPairs = set()
    _temp = 0
    for i in range(start,toEnd):
        
        if(algo=="bf"):
            _temp = AmicableNumber(i,True)
        elif(algo=="Walter_Borough"):
            _temp = Walter_Borough(i)
        
        if(_temp != None):
            allPairs.add(_temp)

    if(toPrint):
        print({tuple(sorted(item)) for item in allPairs})
    else:
        return {tuple(sorted(item)) for item in allPairs}
    
def doTest(toPrint=False,toProgress=False,start=2,toEnd=1000,algo="bf"):
    s=set()
    KK=10000
    from IPython.display import clear_output
    for i in range(start,toEnd+1):
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            clear_output(wait=True)
            print(i,end="\t")
        if(algo=="bf"):
            amc=AmicableNumber(i,True)
        elif(algo=="Walter_Borough"):
            amc=Walter_Borough(i)
        elif(algo=="Sabita_ibn_Kurra"):
            amc=Formula_Sabita_ibn_Kurra(i)
        if(amc):
            s.add(amc)
            if(toPrint and not toProgress):
                print(amc,end=", ")
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            print(s)
    if(not toPrint):
        return s
                
#AmicableNumber(220)
#Formula_Sabita_ibn_Kurra(220)
#Walter_Borough(220)
#doTest(True,False,2,1000,"Walter_Borough")
#doTest(True,False,2,10,"Sabita_ibn_Kurra")

#doTest(True) #10 s