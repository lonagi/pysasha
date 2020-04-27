#Factorization of Numbers and Multi.Partition

def _getProduct(prod):
    res=1
    for i in prod:
        res *= i
    return res
    
def doMPartitionToN(num,to=2,factorization=False):
    import itertools
    s=set()
    for j in itertools.product(*[range(1,num+1) for i in range(to)]):
        if(_getProduct(j)==num and j.count(1)<2):
            s.add(j)
    if(factorization):
        return s
    else:
        return {tuple(sorted(x)) for x in s if(_getProduct(x)==num) }

def doMPartition(num,factorization=False):
    parts=set()
    i=0
    while True:
        i+=1
        d=doMPartitionToN(num,i,factorization)
        if(len(d)==0):
            break
        else:
            parts=parts.union(d)
    return parts

def doTest(toPrint=False,toProgress=False,start=1,toEnd=1000,algo="partition"):
    s=dict()
    KK=10000
    from IPython.display import clear_output
    for i in range(start,toEnd+1):
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            clear_output(wait=True)
            print(i,end="\t")
        if(algo=="partition"):
            pp=doMPartition(i)
        elif(algo=="factorization"):
            pp=doMPartition(i,True)
        if(pp):
            s[i]=pp
            if(toPrint and not toProgress):
                print(i,"-",pp,end=", ")
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            print(s)
    if(not toPrint):
        return s


#doMPartitionToN(125,3)
#doMPartition(8,True)
#doTest(True,False,1,10)
#doTest(True,False,1,10,"factorization")