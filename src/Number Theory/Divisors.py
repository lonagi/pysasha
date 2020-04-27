#Functions of divisors

#Find All divisors for your number
def Divisors(num): 
    from math import sqrt as mmsq
    s=set([1])
    i=1
    a=int(mmsq(num)+1)
    while i<=a: 
        if(num//i==num):
            i+=1
            continue
        if (num%i==0): 
            if (num//i!=i): 
                s.add(num//i)
            s.add(i)
        i+=1
    return s

#the number of the divisors of number
def NumberOfDivisors(num):
    return len(Divisors(num))+1

#the sum of all the divisors of σ(number):
def SumOfDivisors(num):
    return sum(Divisors(num))+num

#the aliquot sum s(number) of proper divisors
def aSumOfDivisors(num):
    return sum(Divisors(num))
    
#print(NumberOfDivisors(12)) #6
#print(SumOfDivisors(12))    #28
#print(aSumOfDivisors(12))   #16