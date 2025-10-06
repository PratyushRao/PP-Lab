def minmax(l):
    l.sort()
    return [l[0],l[-1]]

l = [4,2,3,4,1,3,1]
print(minmax(l))