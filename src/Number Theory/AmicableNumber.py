#Amicable numbers

#Brute force Method
def AmicableNumber():
    ##Start loop from...
    start = 1

    ##Target for loop is...
    purpose = 30000

    ##All divisors for all numbers
    allDels = dict()

    ##First number
    for k in range(start,purpose+1):            

        ##Second number is greater than first number
        for i in range(k,int( (purpose+1)/3 )):

            ##We don't want repeat operations
            ##We search all divisors
            if(str(i) not in allDels):
                allDels[str(i)] = set([1])
                for j in range(2,int((purpose+1)/2)+1):
                    if(i!=j and i%j==0):
                        allDels[str(i)].add(j)

            ##Sum1 = 1st_num and Sum2 = 2nd_num
            if(i != k and sum(allDels[str(i)]) == k and sum(allDels[str(k)]) == i):
                print(i,k)