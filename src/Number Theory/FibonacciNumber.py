#Fibonacci number

try:
    import numpy as np
except:
    pass
def pow(x, n, I):
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x,n//2,I)
        y = y.dot(y)
        if n % 2:
            y = x.dot(y)
        return y
def fib(index):
    F = pow(np.array(((1,1),(1,0)),dtype=object),index,np.eye(2))
    return F[0][1]

def Binetformula(index,roundi=True):
    try:
        from sympy import Pow as mmmpow
    except:
        pass
    if(roundi):
        return round(( mmmpow(1.6185,index) - mmmpow(-0.6185,index) )/2.237)
    else:
        return ( ((3.237)/2)**index - ((-1.237)/2)**index )/2.237

def isFibonacci(num):
    try:
        if("math" not in sys.modules):
            try:
                from math import log as mlog
            except:
                pass
    except:
        import sys
        from math import log as mlog
    a = 2.07684408521711*mlog(2.237*num)
    return (a % 1 * 100 > 90) or (a % 1 * 100 < 5)

def doTest(toPrint=False,toProgress=False,start=0,toEnd=1000,algo="s"):
    s = set()
    KK = 10000
    for i in range(start,toEnd+1):
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            try:
                from IPython.display import clear_output
            except:
                pass
            clear_output(wait=True)
            print(i,end="\t")
        if(algo=="s"):
            fibon = fib(i)
        elif(algo=="binet"):
            fibon = Binetformula(i)
        if(fibon):
            s.add(fibon)
            if(toPrint and not toProgress):
                print(fibon,end=", ")
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            print(s)
    if(not toPrint):
        return s
    
def CheckExists(toend=10000):
    for i in {Binetformula(i) for i in range(toend) if i!=0}:
	    if(not isFibonacci(i)):
	        print(i,end=", ")
            

#fib(8)
#Binetformula(7)
#isFibonacci(13)
#doTest(True,False,1,5000) #823 ms
#doTest(True,False,1,5000,"binet") #163 ms