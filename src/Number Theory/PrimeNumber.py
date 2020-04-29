# Find Prime Numbers

#One
def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def StudentMethod(n):
    lst=[]
    k=0
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                k=k+1
        if k==0:
            lst.append(i)
        else:
            k=0
    return lst

def _bf1(n):
    lst=[]
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            lst.append(i)
    return lst

def _bf2(n):
    lst=[]
    for i in range(2,n+1):
        for j in lst:
            if i%j==0:
                break
        else:
            lst.append(i)
    return lst

def _bf3(n):
    from math import sqrt
    lst=[]
    for i in range(2,n+1):
        for j in lst:
            if j>int((sqrt(i))+1):
                lst.append(i)
                break
            if (i%j==0):
                break
        else:
            lst.append(i)
    return lst

def _bf4(n):
    from math import sqrt
    lst=[]
    for i in range(2,n+1):
        if (i>10):
            if (i%2==0) or (i%10==5):
                continue
        for j in lst:
            if j>int((sqrt(i))+1):
                lst.append(i)
                break
            if (i%j==0):
                break
        else:
            lst.append(i)
    return lst

def _bf5(n):
    from math import sqrt
    lst=[2]
    for i in range(3,n+1,2):
        if (i>10) and (i%10==5):
            continue
        for j in lst:
            if j>int((sqrt(i))+1):
                lst.append(i)
                break
            if (i%j==0):
                break
        else:
            lst.append(i)
    return lst

def _bf6(n):
    lst=[2]
    for i in range(3,n+1,2):
        if (i>10) and (i%10==5):
            continue
        for j in lst:
            if j*j-1>i:
                lst.append(i)
                break
            if (i%j==0):
                break
        else:
            lst.append(i)
    return lst

#Get Sieve of Eratosthenes sequence
def SieveofEratosthenes(n=5):
    a = list(range(n+1))
    a[1]=0
    lst = []
    i=2
    while i<=n:
        if a[i]!=0:
            lst.append(a[i])
            for j in range(i,n+1,i):
                a[j]=0
        i+=1
    return (lst)
    
def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]
    
#SieveofEratosthenes(1000)