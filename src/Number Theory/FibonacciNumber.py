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

def Binetformula(index):
    return round((((5**1/2 + 1)/2)**index)/(5**1/2))

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

#fib(8)
#doTest(True,False,1,5000) #823 ms
#Binetformula(5)
#doTest(True,False,1,5000,"binet") #163 ms