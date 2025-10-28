l=[1,2,3,3,4,5,6,6,7,8,9,9]
sol=[]
for i in l:
    if (l.count(i)>1 and i not in sol):
        sol.append(i)
print(sol)