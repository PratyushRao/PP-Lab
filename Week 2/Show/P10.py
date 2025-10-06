n=int(input("Enter the number: "))
isPrime=True
for i in range(2,n):
    if n%i==0:
        isPrime=False
        break
    
if isPrime:
    print(n," is Prime")
else:
    print(n," is not Prime")