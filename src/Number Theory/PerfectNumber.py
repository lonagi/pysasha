#Find Perfect Numbers

##TOOLS
def Divisors(num):
    s = set([1])
    for i in range( int(num/2 + 1),1,-1):
        if(i!=num and num%i==0):
            s.add(i)
    return s

##THE PROGRAM
def PerfectNumber(num):
    d = Divisors(num)
    return sum(d)==num
             
def doTest(toPrint=False,isPerfect=True,toProgress=False,start=2,toEnd=1000):
    s = set()
    for i in range(start,toEnd):
        if(toProgress and i % 100 == 0):
            try:
                from IPython.display import clear_output
            except:
                pass
            clear_output(wait=True)
            print(i,end="\t")
        if((PerfectNumber(i) and isPerfect) or (not PerfectNumber(i) and not isPerfect) ):
            s.add(i)
            if(toPrint and not toProgress):
                print(i,end=", ")
        if(toProgress and i % 100 == 0):
            print(s)
    return s
            
doTest(True,True,True,2,20000) #All perfect numbers
print("")
doTest(True,False,False,2,10000) #All non perfect numbers