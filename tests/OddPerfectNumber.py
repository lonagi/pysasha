#DO YOU WANT TO FIND ODD PERFECT NUMBER?????????????
#m - almost perfect number
#n - Descartes number

startPower = 300
endPower = 500000

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

n = False
for m in [2**i for i in range(startPower,endPower)]:
    s = set([1])
    for i in range( int(m/2 + 1),1,-1):
        if(m%i==0):
            s.add(i)
    if(sum(s)==2*m - 1):
        n = (2*m - 1) * m
        print(n)
        d=1+4*n
        m2_1 = (1-d**1/2)/2
        m2_2 = (1+d**1/2)/2
        if( (m2_1.is_integer() and isPrime(m2_1)) or m2_2.is_integer() and isPrime(m2_2) ):
            print(n,"IS Odd Perfect Number")