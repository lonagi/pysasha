#Betrothed Numbers

##Brute force Method
def BetrothedNumber(k,ratio=5.5,ratio2=5.5,order=1,returni=False):  
    ##All divisors for all numbers
    allDels = dict()
    
    ###Second number is greater than first number
    try:
        from itertools import chain
    except:
        pass
    
    concatenated = chain( range(k, int(k*ratio)+1 ),range(k, int(k/ratio2)+1 ,-1) )
    for i in concatenated:

        ###We don't want repeat operations
        ###Therefore search and save all divisors
        if(str(i) not in allDels):
            allDels[str(i)] = set([1])
            for j in range(int(k/2+1),1,-1):
                if(i!=j and i%j==0):
                    allDels[str(i)].add(j)

        ###Sum1+order_num = 2nd Num and Sum2+order_num = 1st Nub
        if(i != k and sum(allDels[str(i)]) == k+order and sum(allDels[str(k)]) == i+order):
            if(returni):
                return (k,i)
            else:
                print(k,"->",i)

def BetrothedNumbers(m,n,order=1):
    if(m!=n):
        s1 = set([1])
        for i in range(int(m/2+1),1,-1):
            if(m%i==0):
                s1.add(i)
        s2 = set([1])
        for i in range(int(n/2+1),1,-1):
            if(n%i==0):
                s2.add(i)
        return sum(s1)+m == m+n+1 and sum(s2)+n == sum(s1)+m
    else:
        return False

def doTest(toPrint=False,start=2,toEnd=1000,algo="1"):
    allPairs = set()
    _temp = 0
    
    if(algo=="1"):
        for i in range(start,toEnd):
            if(i < 100000):
                _temp = BetrothedNumber(i,5.5,5.5,1,True)
            else:
                _temp = BetrothedNumber(i,2.5,2.5,1,True)
                
            if(_temp != None):
                allPairs.add(_temp)
    else:    
        for i in range(start,toEnd):
            for j in range(start,toEnd):
                _temp = ((i,j), BetrothedNumbers(i,j) )
                if(_temp[1]):
                    allPairs.add(_temp)

    if(algo=="1"):
        if(toPrint):
            print({tuple(sorted(item)) for item in allPairs})
        else:
            return {tuple(sorted(item)) for item in allPairs}
    else:
        print(allPairs)
                
#BetrothedNumber(48)
#doTest(True,2,1000)

#BetrothedNumbers(140,195)
doTest(True,2,500,"2")