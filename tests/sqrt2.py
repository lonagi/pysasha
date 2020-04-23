def Binetformula(index,roundi=True):
    try:
        from sympy import Pow as mmmpow
    except:
        pass
    q = 2**(1/2)
    r = ( mmmpow(1+q ,index) - mmmpow(1-q,index) )/(2*q)
    if(roundi):
        return round(r)
    else:
        return r
###############################    

def Test1():
    a = list(map(int,sorted(doTest(False,True,0,50,"companion"))))
    b = list(map(int,sorted(doTest(False,True,0,50,"binet"))))
    for i in range(len(a)):
        c = a[i]/b[i]
        print(c, end=", ")
        
def Test2(toEnd=100,allP=True):
    for i in range(1,toEnd):
        a=Binetformula(i)
        q=2**(1/2)
        b=round(a*q)
        if(allP):
            print(b/a,int(b)/int(a))
        else:
            print(int(b)/int(a),end=", ")

Test2(100,False)