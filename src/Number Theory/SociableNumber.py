#Sociable number

#TOOLS
def Divisors(num): 
    from math import sqrt as mmsq
    s=set([1])
    i=1
    a=int(mmsq(num)+1)
    while i<=a: 
        if(num//i==num):
            i+=1
            continue
        if (num%i==0): 
            if (num//i!=i): 
                s.add(num//i)
            s.add(i)
        i+=1
    return s
###########################

#Returns number and periods
def SociableNumber(num,minIt=1,maxIt=20,sequence=False):
    num1=num
    iterat=0
    if(sequence):
        seq=[]
    while iterat<maxIt:
        iterat+=1
        if(sequence):
            seq.append(num)
        
        num = sum(Divisors(num))
        if(num==1):
            return False
        
        if(num1==num):
            if(iterat!=minIt):
                return False
            if(sequence):
                return (num,iterat,seq)
            else:
                return (num,iterat)

def _SociableNumber(num,sequence=False):
    num1=num
    iterat=0
    if(sequence):
        seq=[]
    while True:
        iterat+=1
        if(sequence):
            seq.append(num)
        
        num = sum(Divisors(num))
        if(num==1):
            return False
        
        if(num1==num):
            if(sequence):
                return (num,iterat,seq)
            else:
                return (num,iterat)

def findSociableNumbers(countt):
    komp=[]
    per=[]
    i=0
    while len(komp)<countt:
        i+=1
        for j in range(1,6):
            if(SociableNumber(i,j)):
                komp.append(i)
                per.append(j)
                break
    return (komp,per)
            
            
def doTest(toPrint=False,toProgress=False,start=1,toEnd=1000,algo="s"):
    s=set()
    KK=10000
    from IPython.display import clear_output
    for i in range(start,toEnd+1):
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            clear_output(wait=True)
            print(i,end="\t")
        if(algo=="s"):
            soc=_SociableNumber(i)
        elif(algo=="Amicable"):
            soc=SociableNumber(i,2,2)
        elif(algo=="Perfect"):
            soc=SociableNumber(i,1,1)
        if(soc):
            s.add(soc[0])
            if(toPrint and not toProgress):
                print(soc,end=", ")
        if(toProgress and (i<KK or (i>=KK and i%(KK/100)==0))):
            print(s)
    if(not toPrint):
        return s
    
#SociableNumber(1264460,1,20,True)
#SociableNumber(1264460)
#doTest(False,False,1,5000) #2.35 s

#doTest(False,False,1,10000,"Amicable") #253 ms
#doTest(False,False,1,20000,"Perfect") #361 ms