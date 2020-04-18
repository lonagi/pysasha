#Enumeration of the sum of N terms and all N-k terms
import itertools

num = int(input("Number: "))
terms = int(input("Terms: "))

minterms = terms-1
#minterms = int(input("K: "))

s = set()

for k in range(minterms):
    for j in itertools.product(*[range(1,num+1) for i in range(terms-k)]):
        s.add(j)
    
#Correct Sum and Make Unique data
s = {tuple(sorted(x)) for x in s if(sum(x)==num) }

#Output
print(s)
