def sos(l):
    sum=0
    for i in l:
        sum+=(i**2)
    return sum

l = [1,2,3,4,5]

print(sos(l))