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
            for j in range(k-1,1,-1):
                if(i!=j and i%j==0):
                    allDels[str(i)].add(j)

        ##Sum1 = 1st_num and Sum2 = 2nd_num
        if(i != k and sum(allDels[str(i)]) == k and sum(allDels[str(k)]) == i):
            if(returni):
                return (k,i)
            else:
                print(k,"->",i)    

#AmicableNumber(220)
                
allPairs = set()
_temp = 0
for i in range(2,285):
    _temp = AmicableNumber(i,True)
    if(_temp != None):
        allPairs.add(_temp)
        
allPairs = {tuple(sorted(item)) for item in allPairs}
print(allPairs)