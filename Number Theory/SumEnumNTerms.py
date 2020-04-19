#Enumeration of the sum of N terms
import itertools

num = int(input("Number: "))
terms = int(input("Terms: "))

s = set()

for j in itertools.product(*[range(1,num+1) for i in range(terms)]):
    s.add(j)
    
#Correct Sum and Make Unique data
s = {tuple(sorted(x)) for x in s if(sum(x)==num) }

#Output
print(s)
