#Enumeration of the sum of 2 terms

num = int(input())
s = set()

for i in range(1,num+1):
    s.add( (i,num-i) )   
    
#Make Unique
s = {tuple(sorted(item)) for item in s}

#Output
print(s)
