#Bronze section

def BronzeNumberRatio(toEnd=100):
    pp = (3+13**(1/2))/2
    for i in range(1,toEnd):
        a = i*pp
        if(a%1 *100 <10):
            print((int(a),i),end=', ')

BronzeNumberRatio(100)