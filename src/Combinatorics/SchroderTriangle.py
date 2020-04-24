#Find Schröder Numbers

def getSchroderTriangle(n=5):
    colk = [k for k in range(n+1)]
    a=[[ 1 if(j==0) else 0 for j in colk] for i in colk]
    a[1][1]=2
    for i in range(1,n+1):
        for j in range(1,i+1):
            a[i][j] = a[i][j-1]+a[i-1][j-1]+a[i-1][j]
    
    return a
    
#Schroder Sequence from triangular
def SchroderSequenceFT(n=5,returni=False):
    a = getSchroderTriangle(n)
    b = [[a[i][j] for j in range(len(a[i])) if(i==j) ][0] for i in range(len(a))]
    if(returni):
        return b
    else:
        print(b)

#Schroder Sequence from triangular (method 2)
def SchroderSequenceFT2(n=5,returni=False):
    colk = [k for k in range(n+1)]
    a=[[ 1 if(j==0) else 0 for j in colk] for i in colk]
    b = []
    a[1][1]=2
    for i in range(1,n+1):
        for j in range(i+1):
            if(j==i or j==i-2 or j==i-1):
                a[i][j] = a[i][j-1]+a[i-1][j-1]+a[i-1][j]
                if(i==j):
                    b.append(a[i][j])
            else:
                continue
    return b

#Main numbers from Schroder Sequence
def SchroderSequence(n=5,returni=False):
    a = [1,2]
    for i in range(2,n+2):
        b = 3*a[i-1]
        for k in range(1,i-1):
            b+=a[k]*a[i-k-1]
        a.append(b)
        if(not returni):
            print(b,end=", ")
    if(returni):
        return a
    
#Schroder Sequence by triangular
def SchroderSequenceBT(countt=5,returni=False):
    a = getSchroderTriangle(countt)
    b = [j for sub in a for j in sub if(j!=0)]
    if(returni):
        return b
    else:
        print(b)

def SchroderTriangle(countt=10):
    s = getSchroderTriangle(countt)
    r = range(len(s))
    from pandas import DataFrame as mmpd
    df=mmpd(s, columns=r, index=r)
    df=df.rename_axis(columns="n/k")
    return df

#getSchroderTriangle(5)
#SchroderTriangle()
#SchroderSequence(1000) #525 ms
#SchroderSequenceFT(1000) #384 ms
#SchroderSequenceFT2(1000) #157 ms
#SchroderSequenceBT(200)