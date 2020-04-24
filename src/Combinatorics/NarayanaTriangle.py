#Find Narayana Numbers

def NarayanaNumbers(n,k):
    try:
        from math import factorial as mmfac
    except:
        pass
    
    return int((((mmfac(n))/((mmfac(k-1)) * (mmfac(n-k+1))))/n)*(mmfac(n)/((mmfac(k)*(mmfac(n-k))))))

def printSequence(countt=10):
    for k in range(1,countt):
        for n in range(k,countt):
            print(NarayanaNumbers(n,k),end=", ")
        
def NarayanaTriangle(countt=10):
    colk = [k for k in range(1,countt+1)]
    s=[['' for j in colk] for i in colk]
    for k in range(1,countt+1):
        for n in range(k,countt+1):
            s[n-1][k-1] = NarayanaNumbers(n,k)
            pass
    try:
        import pandas as mmpd
    except:
        pass
    df = mmpd.DataFrame(s, columns=colk, index=colk)
    df =df.rename_axis(columns="n/k")
    return df

#NarayanaNumbers(7,2)            
#printSequence(100)
NarayanaTriangle(10)