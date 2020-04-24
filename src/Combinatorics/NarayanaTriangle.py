#Find Narayana Numbers

def NarayanaNumber(n,k):
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
    
    return _autoFloat((((mmfac(n))/((mmfac(k-1)) * (mmfac(n-k+1))))/n)*(mmfac(n)/((mmfac(k)*(mmfac(n-k))))))

def NarayanaSequence(countt=10,returni=False):
    if(returni):
        s = set()
    for k in range(1,countt):
        for n in range(k,countt):
            if(not returni):
                print(NarayanaNumber(n,k),end=", ")
            else:
                s.add(NarayanaNumber(n,k))
    if(returni):
        return s
        
def NarayanaTriangle(countt=10):
    colk = [k for k in range(1,countt+1)]
    s=[['' for j in colk] for i in colk]
    for k in range(1,countt+1):
        for n in range(k,countt+1):
            s[n-1][k-1] = NarayanaNumber(n,k)
            pass
    from pandas import DataFrame as mmpd
    df = mmpd(s, columns=colk, index=colk)
    df =df.rename_axis(columns="n/k")
    return df

#NarayanaNumber(7,2)
#NarayanaSequence(100)
#NarayanaTriangle(300)