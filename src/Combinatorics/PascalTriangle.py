#Pascal's triangle

def PascalNumber(n,k):
    from math import factorial as mmfac
    from sympy import Float as mmmfloat
    from sympy import Integer as mmmint
    
    def _autoFloat(f):
        from math import log10 as mloggg
        digits = (mloggg(f))+1
        if(digits>15):
            return mmmfloat(f)
        else:
            return mmmint(f)
    
    return _autoFloat(mmfac(n)/(mmfac(k)*mmfac(n-k)))

def PascalSequence(countt=10,returni=False):
    if(returni):
        s = set()
    for n in range(countt):
        for k in range(n+1):
            if(not returni):
                print(PascalNumber(n,k),end=", ")
            else:
                s.add(PascalNumber(n,k))
    if(returni):
        return s
    
def PascalTriangle(countt=10):
    colk = [k for k in range(0,countt)]
    s=[['' for j in colk] for i in colk]
    for k in range(0,countt):
        for n in range(k,countt+1):
            s[n-1][k] = PascalNumber(n,k)
            pass
    from pandas import DataFrame as mmpd
    df = mmpd(s, columns=colk, index=colk)
    df =df.rename_axis(columns="n/k")
    return df
    
#PascalNumber(6,3)
#PascalSequence(100)
#PascalTriangle(200)