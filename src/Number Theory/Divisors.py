#Functions of divisors

def Divisors(num):
    s = set([1])
    for i in range( int(num/2 + 1),1,-1):
        if(i!=num and num%i==0):
            s.add(i)
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
    
print(NumberOfDivisors(12)) #6
print(SumOfDivisors(12))    #28
print(aSumOfDivisors(12))   #16