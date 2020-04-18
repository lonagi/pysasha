#Find Perfect number

def EnumEvenTerms(num):
    res = []
    for i in range(num-1,0,-1):
        if(num%i==0):
            res.append(i)

    if(sum(res)==num):
        print("Num "+str(num)+": ",end="")
        for i in res:
            print(i,end="")
            if(i != res[-1]):
                print("+",end="")
        print("")
            
for i in range(1,1000):
    EnumEvenTerms(i)
