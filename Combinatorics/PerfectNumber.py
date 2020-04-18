#Find Perfect number

def EnumEvenTerms(num, res2 = [], progress=False):
    res = []
    for i in range(num-1,0,-1):
        if(num%i==0):
            res.append(i)
            
    if(progress):
        try:
            from IPython.display import clear_output
        except:
            pass
        
        clear_output(wait=True)
        print("\tNum "+str(num))
        
        for j in res2:
            print("Num "+str(j[0])+": ",end="")
            for i in j[1]:
                print(i,end="")
                if(i != res[-1]):
                    print("+",end="")
            print("")
        
        if(sum(res)==num):
            res2.append( (num,res) )
    else:
        if(sum(res)==num):
            print("Num "+str(num)+": ",end="")
            for i in res:
                print(i,end="")
                if(i != res[-1]):
                    print("+",end="")
            print("")
        return res
    return res2
    
mynumbers = []
for i in range(1,9000):
    mynumbers = EnumEvenTerms(i,mynumbers,True)
