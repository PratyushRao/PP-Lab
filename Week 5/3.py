def isPrime(n: int):
    for i in range(2,n-1):
        if (n%i==0):
            return False
    return True

print(isPrime(5))
print(isPrime(34))