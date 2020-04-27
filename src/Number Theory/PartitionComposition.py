#Partition of Numbers

def _doPartitionTo2(num,composition=False):
    s = set()
    for i in range(1,num):
        s.add( (i,num-i) )   
    if(composition):
        return s
    else:
        return {tuple(sorted(item)) for item in s}
    
#The number of partitions by Hardi
def _CountPartitions(num):
    from math import sqrt,exp,pi
    return (exp(pi*sqrt(2/3)*sqrt(num-1/24)))/(4*num*sqrt(3))

#The number of compositions
def CountCompositions(num):
    return 2**(num-1)
    
def doPartitionToN(num,to=2,composition=False):
    import itertools
    s = set()
    for j in itertools.product(*[range(1,num+1) for i in range(to)]):
        if(sum(j)==num):
            s.add(j)
    if(composition):
        return s
    else:
        return {tuple(sorted(x)) for x in s if(sum(x)==num) }

def doPartition(num,composition=False):
    parts=set()
    i=0
    while True:
        i+=1
        d=doPartitionToN(num,i,composition)
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
            pp=doPartition(i)
        elif(algo=="composition"):
            pp=doPartition(i,True)
        if(pp):
            s[i]=pp
            if(toPrint and not toProgress):
                print(i,"-",pp,end=", ")
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            print(s)
    if(not toPrint):
        return s

#_CountPartitions(1000)
#doPartitionToN(5,5)
#CountCompositions(4)
#doPartition(5)
#doPartition(5,True)
#doTest(True,False,1,5)
#doTest(True,False,1,7,"composition")