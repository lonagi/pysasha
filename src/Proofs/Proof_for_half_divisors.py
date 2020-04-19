#Practical proof of an absence of divisors, which are more than half of this number
#As a result, we don't have any print

#executed in 2.59s, for range(10000)
#The program speed will be 10 longer if range will be 100000

for num in range(10000):
    for i in range(num-1,int(num/2),-1):
        if(num % i == 0):
            print(i)
            break
    