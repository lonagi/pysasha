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

def findSuperPerfectNumbers(save=False,collect=0):
    if(save):
        global spns
    else:
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


spns = []
findSuperPerfectNumbers(True)
