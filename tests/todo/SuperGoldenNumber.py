def SuperGoldenNumber(n=1):
    pp = (1 + ((29 + 3 * (93**(1/2)))/2)**(1/3) + ((29 - 3 * (93**(1/2)))/2)**(1/3))/3
    return round(n*pp)

def SuperGoldenRatio(toEnd=100):
    pp = (1 + ((29 + 3 * (93**(1/2)))/2)**(1/3) + ((29 - 3 * (93**(1/2)))/2)**(1/3))/3
    for i in range(toEnd):
        a = i*pp
        if(a%1 *100 <10):
            print(int(a),"/",i,end=', ')

def isSuperGoldenRectangle(a,b):
    try:
        from math import ceil as cccc
    except:
        pass
    pp = (1 + ((29 + 3 * 93**(1/2))/2)**(1/3) + ((29 - 3 * 93**(1/2))/2)**(1/3))/3
    nn=b
    count=0
    while(nn>0):
        count=count+1
        nn//=10
    return int(cccc((a/b) / (1/10**(count+1)))) * (1/10**(count+1))==int(cccc(pp / (1/10**(count+1)))) * (1/10**(count+1))

#SuperGoldenRatio()
#isSuperGoldenRectangle(145.99)
#SuperGoldenNumber(5)