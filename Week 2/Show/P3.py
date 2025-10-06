a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
cnt=0
for i in range(a,b+1):
    if i %c ==0:
        cnt+=1
        print(i,' is divisibvle by ', c)
print(cnt," Numbers are divisible by ",c)