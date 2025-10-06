def min(list):
    mini=list[0]
    for i in list:
        if i<mini:
            mini=i
    return mini

l = [1,2,3,4,6,2334,2234,-12]

print(min(l))