from math import sqrt as mmmsqrt
def EisensteinTriplet(n,toInv=False):
    s=set()
    fr=0
    if(toInv):
        fr=-n
    for b in range(fr,n):
        for a in range(fr+1, b):
            c=mmmsqrt( a * a + b * b - a*b)
            if c%1==0:
                s.add((a, b, int(c)))
    return s
    
#EisensteinTriplet(5000) #4.19 s