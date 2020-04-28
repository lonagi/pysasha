from math import sqrt as mmmsqrt
def PythagoreanTriplet(n,toInv=False):
    s=set()
    fr=0
    if(toInv):
        fr=-n
    for b in range(fr,n):
        for a in range(fr+1, b):
            c=mmmsqrt( a * a + b * b)
            if c%1==0:
                s.add((a, b, int(c)))
    return s
def PythagoreanTriplet2(limits): 
    c,m=0,2
    s=set()
    while c<limits:
        for n in range(1, m): 
            a=m*m-n*n 
            b=2*m*n 
            c=m*m+n*n
            if c>limits: 
                break
            s.add((a,b,c))
        m = m + 1
    return s
    
#PythagoreanTriplet(5000) #3.46 s
#PythagoreanTriplet2(27000) #19 ms