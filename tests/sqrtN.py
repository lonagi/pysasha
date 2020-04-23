def calcSqr(n):
    for i in range(100):
        a = i*(n**(1/2))
        if(a%1 *100 <10):
            print(int(a),"/",i,end=', ')
calcSqr(5)