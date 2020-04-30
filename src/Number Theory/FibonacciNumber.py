#Fibonacci number

import numpy as np

def __pow(x,n,I):
    if n==0:
        return I
    elif n==1:
        return x
    else:
        y = __pow(x,n//2,I)
        y = y.dot(y)
        if n%2:
            y = x.dot(y)
        return y

def FibonacciNumber(index):
    F = __pow(np.array(((1,1),(1,0)),dtype=object),index,np.eye(2))
    return F[0][1]

def IterationFibonacci(index): 
    a=0
    b=1
    if index == 0: 
        return a 
    elif index == 1: 
        return b 
    else: 
        for i in range(2,index): 
            c=a+b 
            a=b 
            b=c 
        return b
def Binetformula(index,roundi=True):
    from sympy import Pow as mmmpow
    from sympy import Integer as mmmint
    from sympy import N as 
    b = (mmmpow(1.6185,index)-mmmpow(-0.6185,index))/2.237
    if(not roundi):
        return mmmint(b)
    else:
        return mmmn(b)

def isFibonacci(num):
    from math import log as mlog
    a = 2.07684408521711*mlog(2.237*num)
    return (a % 1 * 100 > 90) or (a % 1 * 100 < 5)

def doTest(toPrint=False,toProgress=False,start=0,toEnd=1000,algo="s"):
    s=set()
    KK=10000
    from IPython.display import clear_output
    for i in range(start,toEnd+1):
        if(toProgress and ( i<KK or (i>=KK and i%(KK/100)==0))):
            clear_output(wait=True)
            print(i,end="\t")
        if(algo=="s"):
            fibon=FibonacciNumber(i)
        elif(algo=="binet"):
            fibon=Binetformula(i)
        if(fibon):
            s.add(fibon)
            if(toPrint and not toProgress):
                print(fibon,end=", ")
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            print(s)
    if(not toPrint):
        return s
    
def CheckExists(toend=10000):
    for i in {Binetformula(i) for i in range(toend) if i!=0}:
	    if(not isFibonacci(i)):
	        print(i,end=", ")
            

#FibonacciNumber(8)
#Binetformula(7)
#isFibonacci(13)
#doTest(True,False,1,5000) #823 ms
#doTest(True,False,1,5000,"binet") #163 ms