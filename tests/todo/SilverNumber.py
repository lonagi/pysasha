def SilverNumberRatio(toEnd=100):
    pp = 1+2**(1/2)
    for i in range(1,toEnd):
        a = i*pp
        if(a%1 *100 <10):
            print((int(a),i),end=', ')

#SilverNumberRatio(100)