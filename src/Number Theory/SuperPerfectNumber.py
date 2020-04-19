#Find Superperfect number
def SuperPerfect(n,m=2,k=2):
    num = n
    a = set()
    while m > 0:
        a = set([1,n])
        for j in range(2,n):
            if(n%j==0):
                a.add(j)
        n = sum(a)
        m-=1    
    return sum(a) == k*num

def findSuperPerfectNumbers(collect=0):
    spns = []
    try:
        from IPython.display import clear_output
    except:
        pass

    while True:
        collect+=1
        clear_output(wait=True)
        print(collect)
        print(spns)
        if(SuperPerfect(collect)):
            spns.append(collect)
            
def findAllSuperPerfectNumbers(collect=0,mrange=20,krange=20):
    spns = []
    try:
        from IPython.display import clear_output
    except:
        pass

    while True:
        collect+=1
        for m in range(mrange):
            for k in range(krange):
                clear_output(wait=True)
                print("n=",collect,",m=",m,",k=",k)
                print("(n,m,k)")
                print(spns)
                
                if(SuperPerfect(collect,m,k)):
                    spns.append( (collect,m,k) )

#findSuperPerfectNumbers()
#findAllSuperPerfectNumbers()
