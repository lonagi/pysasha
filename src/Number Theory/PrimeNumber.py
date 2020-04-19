#Prime Number

#One
def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n



#Sieve of Eratosthenes

n = int(input())
a = list(range(n+1))
a[1]=0
lst = []

i=2
while i<=n:
    if a[i]!=0:
        lst.append(a[i])
        for j in range(i,n+1,i):
            a[j]=0
    i+=1
print(lst)