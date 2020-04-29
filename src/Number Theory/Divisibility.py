def Divisibility(nums,divisors):
    s=set()
    for i in range(2,nums+2):
        for j in range(2,divisors+2):
            if(i%j==0):
                s.add( (i,j) )
    return s

#Divisibility(10000,10000)