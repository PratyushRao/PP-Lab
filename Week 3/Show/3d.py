def min(list):
    mini=list[0]
    for i in list:
        if i<mini:
            mini=i
    return mini

def min_idx(list):
    mini=0
    for i in range(len(list)):
        if list[i]<list[mini]:
            mini=i
    return mini


def findNPrint_min(l):
    m = min(l)
    mn_idx=min_idx(l)
    print(m,end=" ")
    l.pop(mn_idx)

l=[2,4,1,3,5,2,21,25]
for i in range(len(l)):
    findNPrint_min(l)

print()