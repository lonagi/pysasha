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

def MatrixFibonacci(index):
    F = __pow(np.array(((1,1),(1,0)),dtype=object),index,np.eye(2))
    return F[0][1]

def MatrixFibonacci2(index):
    return np.linalg.matrix_power(np.matrix(((1,1),(1,0)),dtype=object),index)[0,1]

def RecursionFibonacci(index): 
    if index==1: 
        return 0
    elif index==2: 
        return 1
    else: 
        return RecursionFibonacci(index-1)+RecursionFibonacci(index-2) 

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

def IterationFibonacciSequence(indexLimit): 
    a=0
    b=1
    seq=[0,1]
    if indexLimit == 0: 
        return a 
    elif indexLimit == 1: 
        return [a,b] 
    else: 
        for i in range(2,indexLimit): 
            c=a+b 
            a=b 
            b=c 
            seq.append(b)
        return seq

def Binetformula(index,roundi=True):
    from sympy import Pow as mmmpow
    from sympy import Integer as mmmint
    from sympy import N as mmmn
    b = (mmmpow(1.6185,index)-mmmpow(-0.6185,index))/2.237
    if(not roundi):
        return mmmint(b)
    else:
        return mmmn(b)

def isFibonacci(num):
    from math import log as mlog
    a = 2.07684408521711*mlog(2.237*num)
    return (a % 1 * 100 > 90) or (a % 1 * 100 < 5)

def isFibonacci2(num):
    from math import log as mlog
    a=(mlog(( (num*5**(1/2)+(5*num**2 + 4)**(1/2))/2 ),1.618)+mlog(( (num*5**(1/2)+(5*num**2 - 4)**(1/2))/2 ),1.618))/2
    return (a % 1 * 100 > 99) or (a % 1 * 100 < 1)

def doTest(toPrint=False,toProgress=False,start=0,toEnd=1000,algo="s"):
    s=set()
    KK=10000
    from IPython.display import clear_output
    for i in range(start,toEnd+1):
        if(toProgress and ( i<KK or (i>=KK and i%(KK/100)==0))):
            clear_output(wait=True)
            print(i,end="\t")
        if(algo=="s"):
            fibon=MatrixFibonacci(i)
        elif(algo=="binet"):
            fibon=Binetformula(i)
        elif(algo=="iterat"):
            fibon=IterationFibonacci(i)
        elif(algo=="recursive"):
            fibon=RecursionFibonacci(i)
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
            
def IterationFibonacciWord(index):
    Sn_1 = "0"
    Sn = "01"
    tmp = "" 
    for i in range(2, index + 1): 
        tmp = Sn
        Sn += Sn_1 
        Sn_1 = tmp 
    return Sn 

def FibonacciWord(index):
    from math import floor as mmmfloor
    return ((mmmfloor(index*1.618)-mmmfloor((index+1)*1.618))+2)

#RecursionFibonacci(9)
#IterationFibonacci(9)
#MatrixFibonacci(8)
#MatrixFibonacci2(8)
#Binetformula(7)
#isFibonacci(13)
#doTest(True,False,1,5000) #823 ms
#doTest(True,False,1,5000,"binet") #163 ms