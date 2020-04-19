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
                return (num,iterat)
            break
        
        if(num1==num):
            if(returni):
                return (num,iterat)
            break
            
#SociableNumber(1264460,True,True,True)
#SociableNumber(5,True,True,True)

_temp = 0
for i in range(1,1000000):
    _temp = SociableNumber(i,True,True,True)
    if(_temp[0] == 1):
        continue
    else:
        print(_temp)