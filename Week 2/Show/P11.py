def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print("Prime Nos. are: ",end=" ")
for i in range(100):
    if isPrime(i):
        print(i,end=" ")
        