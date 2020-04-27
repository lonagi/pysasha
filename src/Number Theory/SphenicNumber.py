#Find Sphenic Number
from sympy import isprime
def SphenicNumber(num):
    for i in range(1,num):
        if(num%i==0 and isprime(i)):
            for j in range(1,num):
                if(num%j==0 and isprime(j) and j != i and i*j<num):
                    for k in range(1,num):
                        if(num%k==0 and isprime(k) and k != j and i*j*k==num):
                            return (i,j,k)
    return False
                            
def doTest(toPrint=False,toProgress=False,start=1,toEnd=1000,algo="s"):
    s=set()
    KK=10000
    from IPython.display import clear_output
    for i in range(start,toEnd+1):
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            clear_output(wait=True)
            print(i,end="\t")
        if(algo=="s"):
            soc=SphenicNumber(i)
        if(soc):
            s.add(soc)
            if(toPrint and not toProgress):
                print(i,soc,end=", ")
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            print(s)
    if(not toPrint):
        return s
    
#SphenicNumber(30)
#doTest()