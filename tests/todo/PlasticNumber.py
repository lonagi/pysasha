def PlasticNumber(n):
    pp = (((9+(69**(1/2)))/18)**(1/3))+(((9-(69**(1/2)))/18)**(1/3))
    return round(n*pp)

def PlasticNumberRatio(toEnd=100):
    pp = (((9+(69**(1/2)))/18)**(1/3))+(((9-(69**(1/2)))/18)**(1/3))
    for i in range(1,toEnd):
        a = i*pp
        if(a%1 *100 <10):
            print(int(a),"/",i,end=', ')

#PlasticNumberRatio(100)
#PlasticNumber(80)