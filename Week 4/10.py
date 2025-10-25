#Find common numbers/words between two lists

l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]

s = set()
for i in l1:
    if i in l2:
        s.add(i)
print("Common items are: ", s)