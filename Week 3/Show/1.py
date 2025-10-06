def isPrime(num):
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

num_list = [1,2,3,4,5,6,7,8,9,10]
print("Prime Numbers: ", end=" ")
for i in num_list:
    if isPrime(i):
        print(i, end=" ")