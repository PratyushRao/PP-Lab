a,b=0,1
print(a,b,sep=" ",end=" ")
for i in range(8):
    print(a+b,end=" ")
    a,b=b,a+b