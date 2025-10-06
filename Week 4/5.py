#WAP to print all prime numbers till 0-100

def checkPrime(n:int):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print("Prime Nos. are: ")
for i in range(2,101):
    if checkPrime(i):
        print(i)
