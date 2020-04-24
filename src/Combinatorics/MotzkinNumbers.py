#Find Motzkin Numbers
    
def MotzkinSequence(n=5,returni=False,roundt=True):
    from sympy import Integer as mmmint
    from sympy import Float as mmmfloat
    a = [1,1,2]
    for i in range(3,n+3):
        b = ((((2*i+1)/(i+2))*a[i-1])+(((3*i-3)/(i+2))*a[i-2]))
        if(roundt==True):
            b = mmmint(b)
        else:
            b = mmmfloat(b)
        a.append(b)
        if(not returni):
            print(b,end=", ")
    if(returni):
        return a[:n]
    
#MotzkinSequence(1000,False,False)
#MotzkinSequence(1000,False)