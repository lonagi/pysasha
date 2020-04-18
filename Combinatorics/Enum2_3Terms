#Enumeration of the sum of 2 and 3 terms
num = int(input())
s = set()

for i in range(1,num+1):
    s.add( (i,num-i) )
    for j in range(1,num+1):
        if((num-i-j) > 0):
            s.add( (i,j,num-i-j) )
    
#Make Unique
s = {tuple(sorted(item)) for item in s}

#Output
print(s)
