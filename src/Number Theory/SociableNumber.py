#Sociable number

def SociableNumber(num,returni=False,iteratDebug=False, NumDebug=False):
    if(NumDebug and not returni):
            print(num)
    num1=num
    iterat=0
    while True:
        iterat+=1
        
        #Find all divisors
        allDels = set([1])
        for j in range( int(num/2) ,1,-1):
            if(num%j==0):
                allDels.add(j)
        num = sum(allDels)
        
        if(iteratDebug and not NumDebug):
            if(not returni):
                print(iterat)
        elif(iteratDebug and NumDebug):
            if(not returni):
                print("T",iterat,num)
                
        if(num==1):
            if(returni):
                return False
            break
        
        if(num1==num):
            if(returni):
                return (num,iterat)
            break
            
def doTest(toPrint=False,start=1,toEnd=10000):
    _temp = 0
    allNums = set()
    for i in range(start,toEnd):
        _temp = SociableNumber(i,True,True,True)
        if(_temp != False):
            if(_temp[0] == 1):
                continue
            else:
                if(not toPrint):
                    allNums.add(_temp)
                else:
                    print(_temp)
                    
    if(not toPrint):
        return {tuple(sorted(item)) for item in allNums}
            
#SociableNumber(1264460,True,True,True)
#SociableNumber(27,True,True,True)
print(doTest())
#doTest(True)