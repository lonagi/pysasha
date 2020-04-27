#Find Weird Numbers

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
def AbundantNumber(num):
    return sum(Divisors(num))>num
def SemiPerfectNumber(n):
    factors = Divisors(n)
    if(sum(factors)==n):
        return True)
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
############################

def WeirdNumber(num):
        return (AbundantNumber(num),SemiPerfectNumber(num))

def doTest(toPrint=False,toProgress=False,start=0,toEnd=1000,algo="weird"):
    s=set()
    KK=10000
    from IPython.display import clear_output
    for i in range(start,toEnd+1):
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            clear_output(wait=True)
            print(i,end="\t")
        if(algo=="weird"):
            www=WeirdNumber(i)
        if(www):
            s.add(i)
            if(toPrint and not toProgress):
                print(i,end=", ")
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            print(s)
    if(not toPrint):
        return s

#WeirdNumber(70)
#doTest(True)