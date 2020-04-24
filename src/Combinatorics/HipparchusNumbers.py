#Find Schröder–Hipparchus Numbers
    
def SchroderHipparchusSequence(n=5,returni=False,roundt=True):
    from sympy import Integer as mmmint
    from sympy import Float as mmmfloat
    a = [1,1,3]
    for i in range(3,n+3):
        b = ((6*(i+1)-9)*a[i-1]-(i-2)*a[i-2])/(i+1)
        if(roundt==True):
            b = mmmint(b)
        else:
            b = mmmfloat(b)
        a.append(b)
        if(not returni):
            print(b,end=", ")
    if(returni):
        return a[:n]
    
#SchroderHipparchusSequence(10,False,False)
#SchroderHipparchusSequence(10,True)