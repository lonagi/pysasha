#Enumeration of the product of N terms and all N-k terms
import itertools

def getProduct(tulpa):
    res = 1
    for i in tulpa:
        res *= i
    return res

num = int(input("Number: "))
terms = int(input("Terms: "))

minterms = terms-1
#minterms = int(input("K: "))

s = set()

for k in range(minterms):
    for j in itertools.product(*[range(2,num+1) for i in range(terms-k)]):
        s.add(j)
    
#Correct Product and Make Unique data
s = {tuple(sorted(x)) for x in s if(getProduct(x)==num) }

#Output
print(s)
