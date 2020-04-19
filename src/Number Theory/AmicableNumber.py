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
                
def Formula_Sabita_ibn_Kurra(n):
    def _isPrime(n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n
    
    p = (3 * 2**(n-1)) - 1
    q = (3 * 2**n) - 1
    r = (9 * 2**(2*n-1))-1
    
    if(_isPrime(p) and _isPrime(q) and _isPrime(r)):
        return ( 2**n * p * q, 2**n * r )

def doTest(toPrint=False,start=2,toEnd=1000):
    allPairs = set()
    _temp = 0
    for i in range(start,toEnd):
        _temp = AmicableNumber(i,True)
        if(_temp != None):
            allPairs.add(_temp)

    if(toPrint):
        print({tuple(sorted(item)) for item in allPairs})
    else:
        return {tuple(sorted(item)) for item in allPairs}
                
#AmicableNumber(220)
#doTest(True)