#Find Square triangular numbers

#Square Triangular Number by Euler Formula
def SquareTriangularNumber(k,res="N",roundi=True):
    if(res=="N"):
        r=((((3 + 2 * (2)**(1/2))**(k))-((3 - 2 * (2)**(1/2))**(k)))/(4 * (2)**(1/2)))**2
    elif(res=="t"):
        r=(((3 + 2 * (2)**(1/2))**(k))-((3 - 2 * (2)**(1/2))**(k)) - 2)/(4)
    elif(res=="s"):
        r=(((3 + 2 * (2)**(1/2))**(k))-((3 - 2 * (2)**(1/2))**(k)))/(4 * (2)**(1/2))
    if(roundi):
        return round(r)
    else:
        return r

def doTest(toPrint=False,toProgress=False,start=0,toEnd=1000,algo="euler"):
    s = set()
    KK = 10000
    for i in range(start,toEnd+1):
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            try:
                from IPython.display import clear_output
            except:
                pass
            clear_output(wait=True)
            print(i,end="\t")
        if(algo=="euler"):
            sqrnn = SquareTriangularNumber(i)
        if(algo=="t"):
            sqrnn = SquareTriangularNumber(i,"t")
        if(algo=="s"):
            sqrnn = SquareTriangularNumber(i,"s")
        if(sqrnn):
            s.add(sqrnn)
            if(toPrint and not toProgress):
                print(sqrnn,end=", ")
        if(toProgress and ( i < KK or (i>=KK and i % (KK/100) == 0)) ):
            print(s)
    if(not toPrint):
        return s    
    
#SquareTriangularNumber(2)
#doTest(True,True,0,100)
#SquareTriangularNumber(3,"s")
#sorted(doTest(False,False,0,100,"t"))
#sorted(doTest(False,False,0,100,"s"))