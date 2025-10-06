def comp(l1,l2):
    lr=[]
    for i in l1:
        if i in l2:
            lr.append(i)
    return lr


l1 = [1,2,3,4,5,6,7,8,9]
l2 = [2,3,5,3,1,5,6]

print(comp(l1,l2))