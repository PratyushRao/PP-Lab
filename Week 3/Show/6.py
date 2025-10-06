def avg(l):
    sum=0
    for i in l:
        sum+=i
    return sum/len(l)

l =[1,2,3,4,5,6]

print(avg(l))