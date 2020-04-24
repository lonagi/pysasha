#Find Delannoy Numbers

def getDelannoyArray(n=5):
    colk = [k for k in range(n+1)]
    a=[[ 1 if(j==0 or i==0) else 0 for j in colk] for i in colk]
    a[1][1]=3
    for i in range(1,n+1):
        for j in range(1,n+1):
            a[i][j] = a[i-1][j]+a[i-1][j-1]+a[i][j-1]
    
    return a

#Delannoy Sequence from array
def DelannoySequenceFT(n=5,returni=False):
    a = getDelannoyArray(n)
    b = [[a[i][j] for j in range(len(a[i])) if(i==j) ][0] for i in range(len(a))]
    if(returni):
        return b
    else:
        print(b)

#Delannoy Sequence from array (method 2)
def DelannoySequenceFT2(n=5,returni=False):
    colk = [k for k in range(n+1)]
    a=[[ 1 if(j==0 or i==0) else 0 for j in colk] for i in colk]
    a[1][1]=3
    b=[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(1==1):
                a[i][j] = a[i-1][j]+a[i-1][j-1]+a[i][j-1]
                if(i==j):
                    b.append(a[i][j])
            else:
                continue
    return b

#Central numbers from Delannoy Sequence
def DelannoySequence(n=5,returni=False,roundt=True):
    from sympy import Integer as mmmint
    from sympy import Float as mmmfloat
    a = [1,3]
    for i in range(2,n+2):
        b = (3*(2*i-1)*a[i-1]-(i-1)*a[i-2])/i
        if(roundt==True):
            b = mmmint(b)
        else:
            b = mmmfloat(b)
        a.append(b)
        if(not returni):
            print(b,end=", ")
    if(returni):
        return a[:n]
    
def DelannoArray(countt=10):
    s = getDelannoyArray(countt)
    r = range(len(s))
    from pandas import DataFrame as mmpd
    df=mmpd(s, columns=r, index=r)
    df=df.rename_axis(columns="n/k")
    return df
    
#getDelannoyArray()
#DelannoArray()
#DelannoySequenceFT2(2000) # 3.26 s
#DelannoySequenceFT(2000) #3.12 s
#DelannoySequence(2000) #387 ms