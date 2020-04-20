#Practical proof of fact, that numbers 2^x are almost perfect number

#END = 30
END = int(input("End of loop"))

for i in range(2,END):
    s = set([1])
    n = 2**i
    for j in range(int(n/2+1),1,-1):
        if(n % j==0):
            s.add(j)
    print(n,end=" - ")
    print(sum(s)+1==n)

#OUTPUT
"""
4 - True
8 - True
16 - True
32 - True
64 - True
128 - True
...
2^i - True
"""