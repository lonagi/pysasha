#Amicable numbers

#Brute force Method
def AmicableNumber(k,returni=False):  
    ##All divisors for all numbers
    allDels = dict()
    
    ##Second number is greater than first number
    try:
        from itertools import chain
    except:
        pass
    concatenated = chain( range(k, int(k*2.5)+1 ),range(k, int(k/3)+1 ,-1) )
    for i in concatenated:

        ##We don't want repeat operations
        ##We search all divisors
        if(str(i) not in allDels):
            allDels[str(i)] = set([1])
            for j in range(int(k/2),1,-1):
                if(i!=j and i%j==0):
                    allDels[str(i)].add(j)

        ##Sum1 = 1st_num and Sum2 = 2nd_num
        if(i != k and sum(allDels[str(i)]) == k and sum(allDels[str(k)]) == i):
            if(returni):
                return (k,i)
            else:
                print(k,"->",i)

def _isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n                
                
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
                
#AmicableNumber(220)
#doTest(True)
#doTest(True,2,46,"Walter_Borough")