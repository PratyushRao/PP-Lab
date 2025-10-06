def min(list):
    mini=0
    for i in range(len(list)):
        if list[i]<list[mini]:
            mini=i
    return mini

l = [1,2,3,4,6,2334,2234,-12]

print(min(l))